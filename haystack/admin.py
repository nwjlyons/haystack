from django.contrib import admin

from haystack.models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'clearance_status', 'updated_at']
