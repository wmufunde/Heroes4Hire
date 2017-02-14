
from django.contrib import admin

# Register your models here.
from .models import Hero, Stats, Team, Alias

admin.site.register(Hero)
admin.site.register(Stats)
admin.site.register(Team)
admin.site.register(Alias)