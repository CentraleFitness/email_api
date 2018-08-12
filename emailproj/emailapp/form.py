from django import forms

class OptForm(forms.Form):
    opt_general = forms.BooleanField()
    opt_sales = forms.BooleanField()
    opt_new = forms.BooleanField()
