from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from missions.models import Status

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['heroID', 'missionID']