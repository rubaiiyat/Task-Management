from  django import forms
from .models import addTask

class addForm(forms.ModelForm):
    class Meta:
        model=addTask
        fields='__all__'
        labels={

            'taskTitle':'Task Title',
            'taskDescription':'Task Description',
            'boolean':'Check',
            'date':'Date',
        }
        widgets={
            'date':forms.DateInput(attrs={
                'type':'date',
            
            })
        }
            
        
