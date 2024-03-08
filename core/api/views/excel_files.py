from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.viewsets import GenericViewSet

from core.api.paginations.limit_of_set import DefaultLimitOffSetPagination
from core.api.serializers.excel.excel import ExcelFileSerializer
from core.api.serializers.excel.excel_create import ExcelFileCreateSerializer
from core.api.serializers.excel.excel_detail import ExcelFileDetailSerializer
from core.api.serializers.excel.excel_update_series import ExcelFileSeriesDeleteSerializer
from core.api.serializers.excel.excel_update_series_value import ExcelFileSeriesValueUpdateSerializer
from core.api.serializers.excel.hierarchical_data import ExcelFileHierarchicalSerializer
from core.models import Device, DeviceType, ExcelFile, Series, Value
from core.api.views.helper.delete_excel_file import delete_excel
from django.db.models import F, Prefetch

class ExcelFileViewSet(
    GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
):
    """
    A ViewSet for managing Excel files.

    This ViewSet provides CRUD operations for Excel files, along with additional actions for updating and deleting series.
    """

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "excel-file"
    pagination_class = DefaultLimitOffSetPagination
    lookup_field = "pk"

    def get_serializer_class(self):
        """
        Returns the appropriate serializer class based on the action and request method.
        """
        if self.action == "update_series_value":
            if self.request.method in ["PUT"]:
                return ExcelFileSeriesValueUpdateSerializer
        elif self.action == "delete_series":
            if self.request.method == "POST":
                return ExcelFileSeriesDeleteSerializer
        if self.request.method == "POST":
            return ExcelFileCreateSerializer
        elif self.request.method == "GET" and self.kwargs.get("pk"):
            return ExcelFileDetailSerializer
        else:
            return ExcelFileSerializer

    def get_serializer_context(self):
        """
        Returns the serializer context based on the action.
        """
        if self.action in ["delete_series", "update_series_value"]:
            return {"request": self.request, "user": self.request.user}
        return {"request": self.request}

    def get_queryset(self):
        """
        Returns the queryset for ExcelFile objects based on the request method and action.
        """
        if self.request.method == "GET" and (self.kwargs.get("pk") or self.action in ["hierarchical_data"]):
            queryset = ExcelFile.objects.prefetch_related(
                Prefetch("excel_device", queryset=Device.objects.select_related("excel_file")),
                Prefetch("excel_device_type", queryset=DeviceType.objects.select_related("device__excel_file")),
                Prefetch("excel_device_series", queryset=Series.objects.select_related("excel_file", "device_type__device")),
                Prefetch("excel_device_series_value", queryset=Value.objects.select_related("excel_file", "series__device_type__device"))
            )
            queryset = queryset.order_by("-uploaded_at")
            return queryset
        elif self.request.method == "DELETE" and self.kwargs.get("pk"):
            return ExcelFile.objects.all()
        elif self.action in ["hierarchical_data", "update_series_value", "delete_series"]:
            return ExcelFile.objects.all().order_by("-uploaded_at")
        else:
            return ExcelFile.objects.all().order_by("-uploaded_at")
        

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_excel(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def hierarchical_data(self, request, pk):
        """
        Retrieves hierarchical data for the specified ExcelFile object.
        """
        excel_file = self.get_object()
        serialized_data = ExcelFileHierarchicalSerializer(excel_file).data
        return Response(serialized_data)

    @action(detail=True, methods=['PUT'], url_path='update-series-value')
    def update_series_value(self, request, pk):
        """
        Updates series value for the specified ExcelFile object.
        """
        serializer = ExcelFileSeriesValueUpdateSerializer(data=request.data, context={"request": self.request, "excel_file": self.get_object()})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        update_status = serializer.data.get("status")

        if update_status == "add":
            return Response({"message": "Series value updated successfully"}, status=status.HTTP_200_OK)
        elif update_status == "change":
            return Response({"message": "Series updated successfully"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], url_path='delete-series')
    def delete_series(self, request, pk):
        """
        Deletes series for the specified ExcelFile object.
        """
        serializer = ExcelFileSeriesDeleteSerializer(data=request.data, context={"request": self.request, "excel_file": self.get_object()})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        series_name_data = serializer.data.get("series_name")
        if series_name_data:
            serializer_data = {
                "Message": "Series delete successfully with associated data",
                "series_name": series_name_data
            }
        return Response(serializer_data, status=status.HTTP_204_NO_CONTENT)

