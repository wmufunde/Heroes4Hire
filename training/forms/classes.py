from django.forms import ModelForm
from training.models import ClassTraining

class ClassForm(ModelForm):
    class Meta:
        model = ClassTraining
        fields = ['TrainerID', 'roomID', 'className', 'typeofClass', 'description']