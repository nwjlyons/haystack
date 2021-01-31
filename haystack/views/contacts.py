from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from haystack.clearances import ClearanceStatus
from haystack.forms.contacts import RenameContactForm
from haystack.models import Contact
from haystack.turbo import TurboFormViewMixin


class ContactListView(ListView):
    model = Contact
    ordering = ['-inserted_at']
    template_name = 'contacts/contact_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(clearance_status=ClearanceStatus.APPROVED)


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'


class ContactNameUpdateView(TurboFormViewMixin, UpdateView):
    model = Contact
    form_class = RenameContactForm
    template_name = 'contacts/contact_name_update.html'

    def get_success_url(self):
        return reverse('contact_detail', args=[self.object.id])
