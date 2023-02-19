from django import forms

class newPageForm(forms.Form):
    title = forms.CharField(label="Title: ", widget=forms.TextInput(attrs={
        "class": "form-control w-75 mb-2"
    }))
    description = forms.CharField(label="Description: ", widget=forms.Textarea(attrs={
        "class": "form-control w-75"
    }))