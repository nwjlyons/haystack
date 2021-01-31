from typing import Any

from django.template import Library

from haystack.forms.contacts import ClearanceUpdateForm
from haystack.models import Contact

register = Library()


@register.simple_tag
def clearance_form(*, contact: Contact) -> ClearanceUpdateForm:
    return ClearanceUpdateForm(instance=contact)


@register.inclusion_tag('clearances/clearance_partial.html')
def clearance_partial(*, contact: Contact, form) -> dict[str, Any]:
    return {
        'contact': contact,
        'form': form,
    }
