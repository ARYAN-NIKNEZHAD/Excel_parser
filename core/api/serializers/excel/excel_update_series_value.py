from rest_framework.serializers import Serializer, CharField, ChoiceField, ValidationError, IntegerField
from rest_framework import status
from core.api.serializers.excel.helper.update_excel_status import ExcelUpdateStatus
from core.models import Series, DeviceType, Value
from django.db import transaction
from core.api.views.helper.update_excel_series_value import update_excel_series_value_change
from core.api.views.helper.update_excel_series import update_excel_series_value
from core.api.exceptions.entity_not_found import EntityNotFoundError


class ExcelFileSeriesValueUpdateSerializer(Serializer):
    """
    Serializer for updating the value of a series in an Excel file.
    """

    status = ChoiceField(choices=ExcelUpdateStatus.choices)
    series_name = CharField(max_length=100)
    device_type_id = IntegerField()
    device_type = CharField(max_length=100)
    value = CharField(max_length=200)

    def validate(self, attrs):
        """
        Validate the serializer data.
        """
        excel_file = self.context.get("excel_file")
        update_status = attrs.get("status")
        series_name = attrs.get("series_name")
        device_type = attrs.get("device_type")
        device_type_id = attrs.get("device_type_id")
        value = attrs.get("value")

        # Retrieve the DeviceType object
        device_type = DeviceType.objects.filter(pk=device_type_id, name=device_type).first()
        if not device_type:
            raise EntityNotFoundError("device_type", "device type not found", status_code=status.HTTP_404_NOT_FOUND)
        
        # Retrieve the Series object
        series = Series.objects.filter(name=series_name, excel_file=excel_file, device_type=device_type).first()
        if not series:
            raise EntityNotFoundError("series name", "series not found", status_code=status.HTTP_404_NOT_FOUND)

        return {
            "status": update_status,
            "series_name": series_name,
            "series_obj": series,
            "device_type": device_type,
            "device_type_id": device_type_id,
            "value": value,
        }

    def create(self, validated_data):
        """
        Create a new value or update an existing one in the Excel file.
        """
        with transaction.atomic():
            status = validated_data.get("status")
            excel_file = self.context.get("excel_file")
            series_name = validated_data.get("series_name")
            series = validated_data.get("series_obj")
            value = validated_data.get("value")
            device_type = validated_data.get("device_type")
            device_type_id = validated_data.get("device_type_id")

            if status == ExcelUpdateStatus.ADD:
                update_excel_series_value(excel_file, series_name, device_type, value)
                value_instance = Value.objects.create(excel_file=excel_file, value=value, series=series)
            elif status == ExcelUpdateStatus.CHANGE:
                update_excel_series_value_change(excel_file, series_name, device_type, value)
                series.name = value
                series.save()

            return {
                "series_name": series_name,
                "device_type": device_type,
                "device_type_id": device_type_id,
                "status": status,
                "value": value_instance.value if status == ExcelUpdateStatus.ADD else value,
            }