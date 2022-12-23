from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import SupportTicket

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(SupportTicket, AuthorAdmin)