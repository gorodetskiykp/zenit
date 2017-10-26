from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        #fields = ['short_name', 'full_name', ]       
        exclude = []
