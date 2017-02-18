from django.contrib import admin

# Register your models here.
from .models import Customer, Mission, Report, Status

admin.site.register(Customer)
admin.site.register(Mission)
admin.site.register(Report)
admin.site.register(Status)
