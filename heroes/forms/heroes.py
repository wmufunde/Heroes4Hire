from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from heroes.models import Hero, Stats, Alias


class HeroesForm(ModelForm):
    class Meta:
        model = Hero
        fields = ['codename', 'profilePic']


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['weight', 'height', 'powers', 'intelligence', 'durability', 'strength', 'speed']
        
class AliasForm(ModelForm):
    class Meta:
        model = Alias
        fields = ['firstName', 'surname', 'formerCodeNames', 'occupation', 'address', 'citizenship', 'species']
        

StatsFormSet = inlineformset_factory(Hero, Stats, form=StatsForm, extra=1)

AliasFormSet = inlineformset_factory(Hero, Alias, form=AliasForm, extra=1)
