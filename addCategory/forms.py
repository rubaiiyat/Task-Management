from django import forms
from .models import addCategory

class cateGoryForm(forms.ModelForm):
    class Meta:
        model=addCategory
        fields='__all__'

        