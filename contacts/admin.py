from django.contrib import admin
from .models import Contacts

class ContactsInline(admin.TabularInline):
    model = Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone', 'email')
    search_fields = ('address', 'phone', 'email')
    list_editable = ('address', 'phone', 'email')

