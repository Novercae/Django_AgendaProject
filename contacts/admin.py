from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone_number', 'email',  'category', 'show')
    list_display_links = ('id', 'name', 'last_name')
    # list_filter = ('name', 'last_name')
    list_per_page = 10
    serch_fields = ('name', 'last_name')
    list_editable = ('phone_number', 'show')
    
    

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)