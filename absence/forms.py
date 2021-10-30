from django import forms
from .models import Absence


class AbsenceCreateForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['comment', 'absence_from', 'absence_to']


class AbsenceDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AbsenceDetailForm, self).__init__(*args, **kwargs)
        self.fields['absence_from'].disabled = True
        self.fields['absence_to'].disabled = True
        self.fields['approved'].disabled = True
        self.fields['approved_by'].disabled = True
        self.fields['approved_at'].disabled = True
        self.fields['approved_by_comment'].disabled = True
        self.fields['comment'].disabled = True

    class Meta:
        model = Absence
        fields = '__all__'
        exclude = ['user']
