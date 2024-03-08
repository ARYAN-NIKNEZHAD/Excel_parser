from rest_framework.serializers import ModelSerializer
from core.models.excel_file import ExcelFile
from core.api.views.helper.excel_parser import parse_excel_file

class ExcelFileCreateSerializer(ModelSerializer):
    """
    Serializer for creating ExcelFile objects.
    """

    class Meta:
        model = ExcelFile
        fields = ["file"]

    def create(self, validated_data):
        """
        Create an ExcelFile object by parsing the provided Excel file.
        """
        file = validated_data.get("file")
        excel_file = parse_excel_file(file)
        return excel_file