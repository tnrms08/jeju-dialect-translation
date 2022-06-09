from django import forms

class TransForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)