from django import forms

class CreateAbsenceForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
