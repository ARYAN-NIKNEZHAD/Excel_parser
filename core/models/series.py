from django.db.models import ForeignKey, Model, CASCADE, CharField
from django.utils.translation import gettext_lazy as _

from core.models.device_type import DeviceType
from core.models.excel_file import ExcelFile


class Series(Model):
    """
    Represents a series of values.

    Attributes:
        excel_file (ForeignKey): The associated Excel file.
        device_value (DeviceValue): The device value associated with this series.
        name (str): The name of the series.
    """
    excel_file = ForeignKey(
        ExcelFile,
        db_comment=_("the excel file that associated with this device series"),
        help_text=_("the excel file that associated with this device series"),
        on_delete=CASCADE,
        related_name="excel_device_series"
        )
    device_type = ForeignKey(
        DeviceType,
        db_comment=_("series of a device value"),
        help_text=_("series of a device value"),
        on_delete=CASCADE
        )
    name = CharField(
        verbose_name = _("Name"),
        db_comment = _("name of a device value"),
        help_text = _("name of a device value"),
        max_length=100,
        )
    
