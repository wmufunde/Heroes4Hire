from django.forms import ModelForm
from training.models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['roomName']