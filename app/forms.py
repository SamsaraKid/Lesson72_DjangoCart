from django import forms
from django.core.validators import RegexValidator


class MyForm(forms.Form):
    address = forms.CharField()
    name = forms.CharField()
    phone = forms.CharField(validators=[RegexValidator('[+7][0-9]{10}', message='Неверный номер')])
