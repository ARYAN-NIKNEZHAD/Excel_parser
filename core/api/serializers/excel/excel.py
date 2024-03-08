from rest_framework.serializers import ModelSerializer

from core.models.excel_file import ExcelFile

class ExcelFileSerializer(ModelSerializer):
    """
    Serializer for the ExcelFile model.
    """

    class Meta:
        model = ExcelFile
        fields = ["id", "file", "uploaded_at"]