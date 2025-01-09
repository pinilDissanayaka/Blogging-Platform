from django import forms

class PostCreationForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    check = forms.BooleanField(label="check")