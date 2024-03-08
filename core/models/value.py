from django.db.models import ForeignKey, Model, CASCADE, CharField
from django.utils.translation import gettext_lazy as _

from core.models.series import Series
from core.models.excel_file import ExcelFile


class Value(Model):
    """
    Represents a numerical value in a series.

    Attributes:
        excel_file (ForeignKey): The associated Excel file.
        series (Series): The series to which this value belongs.
        value (float): The numerical value.
    """
    excel_file = ForeignKey(
        ExcelFile,
        db_comment=_("the excel file that associated with this device series values"),
        help_text=_("the excel file that associated with this device series values"),
        on_delete=CASCADE,
        related_name="excel_device_series_value"
        )
    
    series = ForeignKey(
        Series,
        db_comment=_("value of a series"),
        help_text=_("value of a series"),
        on_delete=CASCADE,
        related_name="series_value",
        )
    
    value = CharField(
        verbose_name=_("Value"),
        db_comment=_("the value of a series"),
        help_text=_("the value of a series"),
        editable=True,
    )


