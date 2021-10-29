from django import forms
from .models import Absence


class AbsenceCreateForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['comment', 'absence_from', 'absence_to']

class AbsenceDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbsenceDetailForm, self).__init__(*args, **kwargs)
        self.fields['comment'].disabled = True

    class Meta:
        model = Absence
        fields = '__all__'
