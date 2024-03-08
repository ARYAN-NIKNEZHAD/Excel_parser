from django.db.models import ForeignKey, Model, CASCADE, CharField
from django.utils.translation import gettext_lazy as _

from core.models.device import Device
from core.models.excel_file import ExcelFile


class DeviceType(Model):
    """
    Represents a type of device.

    Attributes:
        excel_file (ForeignKey): The associated Excel file.
        device (Device): The device to which this type belongs.
        name (str): The name of the device type.
    """
    excel_file = ForeignKey(
        ExcelFile,
        db_comment=_("the excel file that associated with this device type"),
        help_text=_("the excel file that associated with this device type"),
        on_delete=CASCADE,
        related_name="excel_device_type"
        )
    
    device = ForeignKey(
        Device,
        db_comment=_("Type of the device"),
        help_text=_("Type of the device"),
        on_delete=CASCADE
        )
    
    name = CharField(
        verbose_name=_("Name"),
        db_comment=_("Name of the device type"),
        help_text=_("Name of the device type"),
        max_length=100,
        )

