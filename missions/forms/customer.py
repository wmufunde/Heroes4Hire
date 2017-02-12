from django.forms import ModelForm
from missions.models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'surname', 'gender', 'address', 'citizenship']