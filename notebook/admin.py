from django.contrib import admin
from django import forms
from .models import Contact, ContactType

class TypeInline(admin.TabularInline):
    model = ContactType

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date Information', {'fields': ['register_date']}),
        (None, {'fields': ['contact_name']}),
    ]

class ContactTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['contact_type']}),
    ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
