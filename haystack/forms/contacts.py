from django import forms
from django.utils.translation import gettext_lazy

from haystack.clearances import opposite_clearance_status
from haystack.forms.base import BaseForm
from haystack.models import Contact


class ClearanceUpdateForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['clearance_status']
        widgets = {
            'clearance_status': forms.widgets.HiddenInput(),
        }

    def __init__(self, *args, instance, **kwargs):
        initial = kwargs.pop('initial', {})
        if 'clearance_status' not in initial:
            initial['clearance_status'] = opposite_clearance_status(instance.clearance_status)
        super().__init__(*args, instance=instance, initial=initial, **kwargs)


class RenameContactForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']
        labels = {
            'name': ''
        }
        widgets = {
            'name': forms.widgets.TextInput(attrs={'placeholder': gettext_lazy("Name this contact …")})
        }
