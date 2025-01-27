from django import forms
from .models import *


class userForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=['firstname','lastname','username','city']