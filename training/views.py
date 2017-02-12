from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from training.forms.attendance import AttendanceForm
from training.forms.classes import ClassForm
from training.forms.trainer import TrainerForm
from training.forms.room import RoomForm

class AttendanceView(FormView):
    template_name = 'attendance.html'
    form_class = AttendanceForm
    success_url = '/training/success/'
    
    def form_valid(self, form):
        form.save()
        super(AttendanceView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
        
class ClassView(FormView):
    template_name = 'class.html'
    form_class = ClassForm
    success_url = '/training/success/'
    
    def form_valid(self, form):
        form.save()
        super(ClassView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)

class TrainerView(FormView):
    template_name = 'trainer.html'
    form_class = TrainerForm
    success_url = '/training/success/'
    
    def form_valid(self, form):
        form.save()
        super(TrainerView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
        
class RoomView(FormView):
    template_name = 'room.html'
    form_class = RoomForm
    success_url = '/training/success'

    
    def form_valid(self, form):
        form.save()
        super(RoomView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)