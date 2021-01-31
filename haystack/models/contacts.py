from django.db import models

from haystack.clearances import ClearanceStatus


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    clearance_status = models.CharField(
        choices=ClearanceStatus.choices,
        default=ClearanceStatus.APPROVED,
        max_length=255
    )
    inserted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_approved(self):
        return self.clearance_status == ClearanceStatus.APPROVED

    def is_denied(self):
        return self.clearance_status == ClearanceStatus.DENIED
