from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile


def validate_excel_file_extension(file: UploadedFile) -> None:
    """
    Validate whether the uploaded file is an Excel file.

    Args:
        file (UploadedFile): The uploaded file object.

    Raises:
        ValidationError: If the file is not an Excel file.
    """
    allowed_extensions = ['xls', 'xlsx']
    file_name = file.name
    file_extension = file_name.split(".")[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValidationError(
            f'The file extension must be one of {", ".join(allowed_extensions)}.'
        )