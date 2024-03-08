from django.db import models
from django.utils.translation import gettext_lazy as _

class ExcelUpdateStatus(models.TextChoices):
    """
    Choices for the status of Excel file updates.
    """
    ADD = "add", _("Add")
    CHANGE = "change", _("Change")