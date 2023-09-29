from django.forms import ModelForm
from django import forms
from .models import Details
from .models import Period

class Messages(ModelForm):
    class Meta:
        model= Details
        fields = ['Messages']
        widget={
            'Messages':forms.Textarea(attrs={'class':'form-control'})
        }

class AddPeriod(ModelForm):
    class Meta:
        model=Period
        fields=['Free','Free_Period_Taken_By']
        '''widget={
            'Free':forms.CheckboxInput(attrs={'class':'form-control'}),
            'Free_Period_Taken_By':forms.ChoiceField(attrs={'class':'form-control'})
        }'''

class TakePeriod(ModelForm):
    class Meta:
        model=Period
        fields=['Name','Free','Free_Period_Taken_By','Time']
    