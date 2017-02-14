from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.template import RequestContext

<<<<<<< HEAD
from heroes.models import Hero, Status, Stats, Team
=======
from heroes.models import Hero, Stats
>>>>>>> 689128ccb8328c08e113466cf7b2a5ce18f4d08b

from heroes.forms.heroes_form import HeroesForm, StatsFormSet, AliasFormSet

from heroes.forms.team import TeamForm
from heroes.forms.status import StatusForm
from heroes.forms.currentteam import CurrentteamForm
from django.contrib.auth.decorators import login_required


class HeroesView(FormView):
    template_name = 'signup.html'
    form_class = HeroesForm
    success_url = '/heroes/successcurrentteam'
    
    def get_context_data(self, **kwargs):
        context = super(HeroesView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['stats_form'] = StatsFormSet(self.request.POST)
            context['alias_form'] = AliasFormSet(self.request.POST)
        else:
            context['stats_form'] = StatsFormSet()
            context['alias_form'] = AliasFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        stats_form = context['stats_form']
        if stats_form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            stats_form.instance = self.object
            stats_form.save()
        alias_form = context['alias_form']
        if alias_form.is_valid():
            alias_form.instance = self.object
            alias_form.save()
        return HttpResponseRedirect(self.success_url)
    
class TeamView(FormView):
    template_name = 'team.html'
    form_class = TeamForm
    success_url = '/heroes/successcurrentteam'
    
    def form_valid(self, form):
        form.save()
        super(TeamView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
class StatusView(FormView):
    template_name = 'status.html'
    form_class = StatusForm
    success_url = '/heroes/successcurrentteam'
    
    def form_valid(self, form):
        form.save()
        super(StatusView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
class CurrentteamView(FormView):
    template_name = 'currentteam.html'
    form_class = CurrentteamForm
    success_url = '/heroes/successcurrentteam'
    
    def form_valid(self, form):
        form.save()
        super(CurrentteamView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
class ProfileView(DetailView):
    template_name = 'profile.html'
    model = Hero
    
class TeamProfileView(DetailView):
    template_name = 'team_profile.html'
    model = Team
    
class PicupdateView(UpdateView):
    template_name = 'picupdate.html'
    success_url = '/heroes/successcurrentteam'
    model = Hero
    fields = ['profilePic']
    
    
 # Update Hero statistics    
class HeroesUpdateView(UpdateView):
    template_name = 'signup.html'
    success_url = '/heroes/successcurrentteam'
    model = Hero
    form_class = HeroesForm
    
    def get_context_data(self, **kwargs):
        context = super(HeroesUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['stats_form'] = StatsFormSet(self.request.POST)
            context['alias_form'] = AliasFormSet(self.request.POST)
        else:
            context['stats_form'] = StatsFormSet(queryset=self.object.status_set)
            context['alias_form'] = AliasFormSet(queryset=self.object.alias_set)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        stats_form = context['stats_form']
        if stats_form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            stats_form.instance = self.object
            stats_form.save()
        alias_form = context['alias_form']
        if alias_form.is_valid():
            alias_form.instance = self.object
            alias_form.save()
        return HttpResponseRedirect(self.success_url)
    
class HeroesDeleteView(DeleteView):
    template_name = 'hero_confirm_delete.html'
    model = Hero
    success_url = '/heroes/hero_list'

@login_required
def profile(request):
    heroes = Hero.objects.filter(user=request.user)
    if heroes:
        hero = heroes[0]
        return HttpResponseRedirect('/heroes/profile/%d' % hero.id)
    else:
        return HttpResponseRedirect('/heroes/heroessignup/')
    

@login_required
def hero_list(request, template='hero_list.html'):
    heroes = Hero.objects.all()
    context = {
        'heroes': heroes,
    }
    return render_to_response(template, context)

@login_required
def team_list(request, template='team_list.html'):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render_to_response(template, context)

class TeamUpdateView(UpdateView):
    template_name = 'team.html'
    success_url = '/heroes/successcurrentteam'
    model = Team
    form_class = TeamForm
    
class TeamDeleteView(DeleteView):
    template_name = 'team_confirm_delete.html'
    model = Team
    success_url = '/heroes/team_list'
    
