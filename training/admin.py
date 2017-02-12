from django.contrib import admin

# Register your models here.
from .models import Trainer, Room, ClassTraining, Attendance, ReportLog

admin.site.register(Trainer)
admin.site.register(Room)
admin.site.register(ClassTraining)
admin.site.register(Attendance)
admin.site.register(ReportLog)