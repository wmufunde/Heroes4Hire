from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, UpdateView

from missions.forms.customer import CustomerForm
from missions.forms.mission import MissionForm
from missions.forms.report import ReportForm
from missions.models import Customer

from django.contrib.auth.decorators import login_required

class CustomerView(FormView):
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = '/missions/customer'
    
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
    
    
    
