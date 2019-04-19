from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from team.models import Team
from .models import Player
from .forms import PlayerCreateForm, RigesterForm

class PlayerListView(ListView):
    def get_queryset(self):
        queryset = Player.objects.all()
        return queryset

class PlayerDetailView(DetailView):
    queryset = Player.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        context["Teams"] =  Team.objects.all().filter(players = kwargs["object"])
        print(context["Teams"])
        
        return context
    
    #TODO search for player in team to list
    #instance = queryset.account
    #teams = instace.team_set.all()

class PlayerCreateView(LoginRequiredMixin, CreateView):
    form_class = PlayerCreateForm
    template_name = 'player/form.html'
    success_url = '/teams/' #go to teams after signing up

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.account = self.request.user
        return super(PlayerCreateView, self).form_valid(form)

class RegisterView(CreateView):
    form_class = RigesterForm
    template_name = 'registration/register.html'
    success_url = '/teams/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect("/logout")
        else:
            return super(RegisterView, self).dispatch(*args, **kwargs)
