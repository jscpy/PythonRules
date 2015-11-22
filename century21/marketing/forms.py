from django import forms
from marketing.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
