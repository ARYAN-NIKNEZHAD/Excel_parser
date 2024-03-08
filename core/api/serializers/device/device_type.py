from rest_framework.serializers import ModelSerializer
from core.api.serializers.device.device import DeviceSerializer
from core.models.device_type import DeviceType

class DeviceTypeSerializer(ModelSerializer):
    """
    Serializer for DeviceType model.
    """
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = DeviceType
        fields = ["id", "excel_file", "device", "name"]
