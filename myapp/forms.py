from django.forms import ModelForm
from .models import Lost, Found

class LostForm(ModelForm):
  
    class Meta:
        model = Lost
        fields = ['name', 'email', 'item', 'description', 'location', 'photo']

class FoundForm(ModelForm):
  
    class Meta:
        model = Found
        fields = ['item', 'description', 'location', 'photo']