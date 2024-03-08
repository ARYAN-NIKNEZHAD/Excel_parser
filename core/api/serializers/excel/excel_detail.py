from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import ExcelFile
from core.api.serializers.device.device import DeviceSerializer
from core.api.serializers.device.device_type import DeviceTypeSerializer
from core.api.serializers.series.series import SeriesSerializer
from core.api.serializers.series.series_value import SeriesValueSerializer

class ExcelFileDetailSerializer(ModelSerializer):
    """
    Serializer for detailed representation of ExcelFile objects.
    """

    device = SerializerMethodField()
    device_types = SerializerMethodField()
    series = SerializerMethodField()
    series_values = SerializerMethodField()

    class Meta:
        model = ExcelFile
        fields = ["id", "file", "uploaded_at", "device", "device_types", "series", "series_values"]

    def get_device(self, file):
        """
        Retrieve and serialize device data associated with the ExcelFile.
        """
        data = file.excel_device.all()
        return DeviceSerializer(data, many=True).data
    
    def get_device_types(self, file):
        """
        Retrieve and serialize device type data associated with the ExcelFile.
        """
        data = file.excel_device_type.all()
        return DeviceTypeSerializer(data, many=True).data
    
    def get_series(self, file):
        """
        Retrieve and serialize series data associated with the ExcelFile.
        """
        data = file.excel_device_series.all()
        return SeriesSerializer(data, many=True).data
    
    def get_series_values(self, file):
        """
        Retrieve and serialize series value data associated with the ExcelFile.
        """
        data = file.excel_device_series_value.all()
        return SeriesValueSerializer(data, many=True).data
    