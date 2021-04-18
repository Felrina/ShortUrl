from shortner.models import UrlModels
from django import forms
from shortner.validators import validate_url

class UrlForms(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url], widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Long URL",}))
    
    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        
