from django import forms
from .models import Userinfo
class PersonForm(forms.Form):
    id = forms.CharField()
    이름 = forms.CharField()
    나이 = forms.CharField()
    직급 = forms.CharField()
    부서 = forms.CharField()