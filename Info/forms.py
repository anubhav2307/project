from django import forms
from .models import user_uploads

class user_form(forms.ModelForm):

    class Meta:
        model = user_uploads
        fields = [
        'file'
        ]


class SearchForm(forms.Form):
    name = forms.CharField(label='Search Mutation', max_length=15)