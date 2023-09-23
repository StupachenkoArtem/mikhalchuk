from django import forms
from mikhalchuk.models import *


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Collections
        fields = ['name', 'photo1']
