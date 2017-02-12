from django.forms import ModelForm
from training.models import Trainer

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = ['firstName', 'surname', 'gender', 'address', 'citizenship']
