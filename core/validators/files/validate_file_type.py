from typing import Union
import mimetypes
from django.core.exceptions import ValidationError


def validate_excel_file_type(value: Union[str, bytes]) -> None:
    """
    Validate file type for Excel files.

    Args:
        value (Union[str, bytes]): The file path or file object to validate.

    Raises:
        ValidationError: If the file is not a valid Excel file.
        TypeError: If allowed_extensions is not a list.
    """
    allowed_extensions = ["xls", "xlsx"]
    if not isinstance(allowed_extensions, list):
        raise TypeError("allowed_extensions must be a list of strings like: ['xls', 'xlsx']")

    try:
        file = value.open("rb") if isinstance(value, str) else value
        file_extension = value.name.split(".")[-1].lower()
        if file_extension not in allowed_extensions:
            raise ValidationError("Invalid file extension. Only allowed extensions are: {}".format(", ".join(allowed_extensions)))

        mime_type, _ = mimetypes.guess_type(value.name)
        if mime_type not in ('application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
            raise ValidationError("Invalid file type. Only Excel files are allowed.")

    finally:
        if isinstance(value, str):
            file.close()