from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Service, ContactRequest

@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    search_fields = ('name', 'phone_number', 'message')
    list_filter = ('created_at',)