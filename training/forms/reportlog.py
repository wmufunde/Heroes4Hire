from django.forms import ModelForm
from training.models import ReportLog

class ReportLogForm(ModelForm):
    class Meta:
        model = ReportLog
        fields = ['classID', 'heroID', 'TrainerID', 'grade', 'outcome', 'comments']