

from django import forms


class NameForm(forms.Form):
    Telephone = forms.CharField(label="Telephone", max_length=100)

