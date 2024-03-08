from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField, CharField

from core.api.serializers.device.device import DeviceSerializer
from core.api.serializers.device.device_type import DeviceTypeSerializer
from core.api.serializers.series.series import SeriesSerializer
from core.api.serializers.series.series_value import SeriesValueSerializer
from core.models import ExcelFile

class ExcelFileHierarchicalSerializer(ModelSerializer):
    """
    Serializer for generating hierarchical data from an ExcelFile object.
    """

    device = SerializerMethodField()
    device_types = SerializerMethodField()
    series = SerializerMethodField()
    series_values = SerializerMethodField()

    class Meta:
        model = ExcelFile
        fields = ["device", "device_types", "series", "series_values"]

    def get_device(self, file):
        """
        Returns serialized data for devices associated with the ExcelFile.
        """
        data = file.excel_device.all()
        return DeviceSerializer(data, many=True).data
    
    def get_device_types(self, file):
        """
        Returns serialized data for device types associated with the ExcelFile.
        """
        data = file.excel_device_type.all()
        return DeviceTypeSerializer(data, many=True).data
    
    def get_series(self, file):
        """
        Returns serialized data for series associated with the ExcelFile.
        """
        data = file.excel_device_series.all()
        return SeriesSerializer(data, many=True).data
    
    def get_series_values(self, file):
        """
        Returns serialized data for series values associated with the ExcelFile.
        """
        data = file.excel_device_series_value.all()
        return SeriesValueSerializer(data, many=True).data
    