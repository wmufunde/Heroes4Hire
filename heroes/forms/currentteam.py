from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from heroes.models import Status

class CurrentteamForm(ModelForm):
    class Meta:
        model = Status
        fields = ['heroID', 'teamID']