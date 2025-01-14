from django.contrib import admin
from app.client.models import Client



class ClientAdmin(admin.ModelAdmin):

    model = Client

    list_display = ('photo', 'name', 'email', 'smartphone')
    search_fields = ('name', 'email', 'smartphone')
    list_filter = ('name', 'email', 'smartphone') 