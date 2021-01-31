from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from haystack.views.contacts import ContactListView, ContactDetailView, ContactNameUpdateView
from haystack.views.clearances import ClearanceListView, ClearanceUpdateView
from haystack.views.settings import SettingsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clearances/', include([
        path('<int:pk>/', ClearanceUpdateView.as_view(), name='clearance_update'),
        path('', ClearanceListView.as_view(), name='clearance_list'),
    ])),
    path('contacts/', include([
        path('<int:pk>/', include([
            path('name/edit/', ContactNameUpdateView.as_view(), name='contact_name_update'),
            path('', ContactDetailView.as_view(), name='contact_detail'),
        ])),
        path('', ContactListView.as_view(), name='contact_list'),
    ])),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('', RedirectView.as_view(pattern_name='clearance_list')),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Static files
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
