from rest_framework.serializers import ModelSerializer
from core.models.device import Device

class DeviceSerializer(ModelSerializer):
    """
    Serializer for Device model.
    """
    class Meta:
        model = Device
        fields = ["excel_file", "name"]