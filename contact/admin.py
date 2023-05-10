from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', 'phone', 'email',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name',
    list_display_links = 'last_name','phone','email',