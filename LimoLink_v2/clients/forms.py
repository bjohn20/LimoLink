from django import forms
from .models import Client

class ClientModelForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = (
      'first_name',
      'last_name',
      'street_address'
    )

class ClientForm(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  street_address = forms.CharField()