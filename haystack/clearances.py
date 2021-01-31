from django.db import models
from django.utils.translation import gettext_lazy


class ClearanceStatus(models.TextChoices):
    APPROVED = 'approved', gettext_lazy("Approved")
    DENIED = 'denied', gettext_lazy("Denied")


def opposite_clearance_status(clearance_status: ClearanceStatus) -> ClearanceStatus:
    if clearance_status == ClearanceStatus.APPROVED:
        return ClearanceStatus.DENIED
    elif clearance_status == ClearanceStatus.DENIED:
        return ClearanceStatus.APPROVED

    raise ValueError(f"unknown {clearance_status=}")
