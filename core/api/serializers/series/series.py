from rest_framework.serializers import ModelSerializer
from core.api.serializers.device.device_type import DeviceTypeSerializer
from core.models.series import Series

class SeriesSerializer(ModelSerializer):
    """
    Serializer for Series model.
    """
    device_type = DeviceTypeSerializer(read_only=True)

    class Meta:
        model = Series
        fields = ["id", "excel_file", "device_type", "name"]