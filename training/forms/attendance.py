from django import forms
from django.forms import ModelForm
from django.conf import settings
from training.models import Attendance

class AttendanceForm(ModelForm):
    classDate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Attendance
        fields = ['heroID','classID', 'roomID', 'classDate', 'startTime', 'endTime']
