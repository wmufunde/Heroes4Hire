from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from missions.forms.customer import CustomerForm
from missions.forms.mission import MissionForm
from missions.forms.report import ReportForm

from missions.models import Customer, Mission

from django.views.generic.edit import FormView, UpdateView

from missions.forms.customer import CustomerForm
from missions.forms.mission import MissionForm
from missions.forms.report import ReportForm
from missions.models import Customer

from django.contrib.auth.decorators import login_required
from django.template import RequestContext

class CustomerView(FormView):
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = '/heroes/successcurrentteam'
    
    def form_valid(self, form):
        form.save()
        super(CustomerView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
class MissionView(FormView):
    template_name = 'mission.html'
    form_class = MissionForm
    success_url = '/missions/mission'
    
    def form_valid(self, form):
        form.save()
        super(MissionView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
class ReportView(FormView):
    template_name = 'report.html'
    form_class = ReportForm
    success_url = '/missions/report'
    
    def form_valid(self, form):
        form.save()
        super(ReportView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
@login_required
def customer_list(request, template='customer_list.html'):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render_to_response(template, context)


class CustomersUpdateView(UpdateView):
    template_name = 'customer.html'
    success_url = '/heroes/successcurrentteam'
    model = Customer
    form_class = CustomerForm
    
class CustomersDeleteView(DeleteView):
    template_name = 'customer_confirm_delete.html'
    model = Customer
    success_url = '/missions/customer_list'
    
@login_required
def mission_list(request, template='mission_list.html'):
    missions = Mission.objects.all()
    context = {
        'missions': missons,
    }
    return render_to_response(template, context)

class MissionProfileView(DetailView):
    template_name = 'mission_profile.html'
    model = Mission
    
    
