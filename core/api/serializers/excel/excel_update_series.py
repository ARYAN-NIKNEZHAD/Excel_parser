from rest_framework.serializers import Serializer, CharField, ValidationError, IntegerField, ReadOnlyField
from django.db import transaction
from core.models import Series, DeviceType
from core.api.views.helper.delete_excel_series import delete_series_from_excel_file
from core.api.exceptions.entity_not_found import EntityNotFoundError
from rest_framework import status


class ExcelFileSeriesDeleteSerializer(Serializer):
    """
    Serializer for deleting a series from an Excel file.
    """

    series_name = CharField(max_length=200)
    device_type = CharField(max_length=200)
    device_type_id = IntegerField()
    series_obj = ReadOnlyField()

    def validate(self, attrs):
        """
        Validate the serializer data.
        """
        excel_file = self.context.get("excel_file")
        series_name = attrs.get("series_name")
        device_type = attrs.get("device_type")
        device_type_id = attrs.get("device_type_id")

        # Retrieve the DeviceType object
        device_type = DeviceType.objects.filter(pk=device_type_id, name=device_type).first()
        if not device_type:
            raise EntityNotFoundError("device_type", "Device type not found", status_code=status.HTTP_404_NOT_FOUND)
        
        # Retrieve the Series object
        series = Series.objects.filter(name=series_name, excel_file=excel_file, device_type=device_type)
        if not series:
            raise EntityNotFoundError("series_name", "Series not found", status_code=status.HTTP_404_NOT_FOUND)
        
        if len(series) == 1:
            series.first()

        return {
            "series_name": series_name,
            "series_obj": series,
            "device_type": device_type,
            "device_type_id": device_type_id,
        }

    def create(self, validated_data):
        """
        Perform the deletion of the series from the Excel file.
        """
        with transaction.atomic():
            excel_file = self.context.get("excel_file")
            series_name = validated_data.get("series_name")
            series = validated_data.get("series_obj")
            device_type = validated_data.get("device_type")
            device_type_id = validated_data.get("device_type_id")
            delete_series_from_excel_file(excel_file, series_name, device_type)
            series.delete()

            return {
                "series_name": series_name,
                "device_type": device_type,
                "device_type_id": device_type_id,
            }

