from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_excel_file_size(value):
    """
    Validate the size of an Excel file.
    
    Args:
        value: Uploaded file object.
    
    Raises:
        ValidationError: If the file size exceeds the maximum allowed size of 50 MB.
    """
    max_size = 50 * 1024 * 1024  # 50 MB in bytes
    if value.size > max_size:
        raise ValidationError(
            _('The file size exceeds the maximum allowed size of 50 MB.')
        )