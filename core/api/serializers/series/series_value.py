from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.api.serializers.series.series import SeriesSerializer
from core.models.value import Value

class SeriesValueSerializer(ModelSerializer):
    """
    Serializer for Value model.
    """
    series = SeriesSerializer(read_only=True)
    value = SerializerMethodField()

    class Meta:
        model = Value
        fields = ["id", "excel_file", "series", "value"]

    def get_value(self, value):
        """
        Method to parse and convert the value to an appropriate data type.
        If the value is numeric (integer or float), it returns the converted value.
        Otherwise, it returns the original value.
        """
        converted_value = ''
        is_float = False
        for char in value.value:
            if char.isdigit() or (char == '.' and not is_float):
                converted_value += char
                if char == '.':
                    is_float = True
            else:
                return value.value  
        try:
            if is_float:
                return float(converted_value)
            else:
                return int(converted_value)
        except ValueError:
            return value.value