from django import forms
from . import util

class newPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        "class": "form-control w-75 mb-2"
    }))
    content = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        "class": "form-control w-75"
    }))

class editPageForm(forms.Form):
    content = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        "class": "form-control w-75",
    }))
