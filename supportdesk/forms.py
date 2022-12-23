from django import forms


from django.forms import ModelForm
from .models import SupportTicket

# Create the form class.
class SupportTicketForm(ModelForm):

    class Meta:
        model = SupportTicket
        fields = ['summary', 'description','is_priority']