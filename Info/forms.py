from django import forms
from .models import user_uploads

class user_form(forms.ModelForm):

    class Meta:
        model = user_uploads
        fields = [
        'file'
        ]