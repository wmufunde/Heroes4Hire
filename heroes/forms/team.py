from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from heroes.models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name','leader','address', 'description', 'members']