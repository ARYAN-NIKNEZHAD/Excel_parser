from django.db.models import Model, FileField, DateTimeField
from django.utils.translation import gettext_lazy as _

from core.validators.files.validate_file_ext import validate_excel_file_extension
from core.validators.files.validate_file_type import validate_excel_file_type
from core.validators.files.validate_file_max import validate_excel_file_size


class ExcelFile(Model):
    """
    Represents an uploaded Excel file.

    Attributes:
        file (FileField): The uploaded Excel file.
        uploaded_at (DateTimeField): The timestamp of when the file was uploaded.
    """
    file = FileField(
        verbose_name=_("File"),
        db_comment=_("uploaded file"),
        help_text=_("uploaded file"),
        upload_to="excel_files/%Y/%m/%d",
        validators=[
            validate_excel_file_type,
            validate_excel_file_extension,
            validate_excel_file_size
        ]
        )
    
    uploaded_at = DateTimeField(
        verbose_name=_("Uploaded_at"),
        db_comment=_("the time to upload the file"),
        help_text=_("the time to upload the file"),
        auto_now_add=True
        )