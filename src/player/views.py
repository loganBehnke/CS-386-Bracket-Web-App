from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Player
from .forms import PlayerCreateForm, RigesterForm

class PlayerListView(ListView):
    def get_queryset(self):
        queryset = Player.objects.all()
        return queryset

class PlayerDetailView(DetailView):
    queryset = Player.objects.all()
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
