from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, UpdateView, DeleteView
from training.forms.attendance import AttendanceForm
from training.forms.classes import ClassForm
from training.forms.trainer import TrainerForm
from training.forms.room import RoomForm

from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

from training.models import ClassTraining, Room, Trainer

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
    
@login_required
def class_list(request, template='class_list.html'):
    classTrainings = ClassTraining.objects.all()
    context = {
        'classTrainings': classTrainings,
    }
    return render_to_response(template, context)

class ClassUpdateView(UpdateView):
    template_name = 'class.html'
    success_url = '/training/success'
    model = ClassTraining
    form_class = ClassForm
    
class ClassDeleteView(DeleteView):
    template_name = 'class_confirm_delete.html'
    model = ClassTraining
    success_url = '/training/class_list'


class ClassProfileView(DetailView):
    template_name = 'class_profile.html'
    model = ClassTraining
    
@login_required
def room_list(request, template='room_list.html'):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render_to_response(template, context)

class RoomUpdateView(UpdateView):
    template_name = 'room.html'
    success_url = '/training/success'
    model = Room
    form_class = RoomForm
    
class RoomDeleteView(DeleteView):
    template_name = 'room_confirm_delete.html'
    model = Room
    success_url = '/training/room_list'

@login_required
def trainer_list(request, template='trainer_list.html'):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers,
    }
    return render_to_response(template, context)

class TrainerUpdateView(UpdateView):
    template_name = 'trainer.html'
    success_url = '/training/success'
    model = Trainer
    form_class = TrainerForm
    
class TrainerDeleteView(DeleteView):
    template_name = 'room_confirm_delete.html'
    model = Trainer
    success_url = '/training/trainer_list'

class TrainerProfileView(DetailView):
    template_name = 'trainer_profile.html'
    model = Trainer
    

    