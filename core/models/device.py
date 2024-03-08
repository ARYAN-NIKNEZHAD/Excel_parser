from django.db.models import ForeignKey, CharField, CASCADE, Model
from django.utils.translation import gettext_lazy as _

from core.models.excel_file import ExcelFile


class Device(Model):
    """
    Represents a device.
    
    Attributes:
        excel_file (ForeignKey): The associated Excel file.
        name (str): The name of the device.
    """
    excel_file = ForeignKey(
        ExcelFile,
        db_comment=_("the excel file that associated with this device"),
        help_text=_("the excel file that associated with this device"),
        on_delete=CASCADE,
        related_name="excel_device"
        )
    
    name = CharField(
        verbose_name=_('Name'),
        db_comment=_("Name of the device"),
        help_text=_("Name of the device"),
        editable=True,
        max_length=100,
        )