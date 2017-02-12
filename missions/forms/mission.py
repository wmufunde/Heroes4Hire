from django.forms import ModelForm
from missions.models import Mission

class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = ['customerID', 'description', 'locations', 'difficulty']