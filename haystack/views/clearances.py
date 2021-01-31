from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from haystack.forms.contacts import ClearanceUpdateForm
from haystack.models import Contact
from haystack.turbo import TurboFormViewMixin


class ClearanceListView(ListView):
    model = Contact
    ordering = ['-inserted_at']
    template_name = 'clearances/clearance_list.html'


class ClearanceUpdateView(TurboFormViewMixin, UpdateView):
    model = Contact
    form_class = ClearanceUpdateForm
    success_url = reverse_lazy('clearance_list')
    template_name = 'clearances/clearance_update.html'
