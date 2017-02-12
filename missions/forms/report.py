from django.forms import ModelForm
from missions.models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['missionID', 'heroID', 'outcome', 'comments']