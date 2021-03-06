from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

from Bracket.models import Bracket, Match

from .models import Team
from player.models import Player
from .forms import TeamCreateForm, JoinTeamForm

# Create your views here.
class TeamCreateView(LoginRequiredMixin , CreateView):
    form_class = TeamCreateForm
    template_name = 'team/form.html'
    #login_url = '/login/' default set in base settings
    success_url = '/teams/'

    def form_valid(self, form):
        instance = form.save(commit = False)
        user = self.request.user
        print(user)
        try:
            player = Player.objects.get(account=user)
            instance.teamCaptin = player
            return super(TeamCreateView, self).form_valid(form)
        except Player.DoesNotExist:
            messages.warning(self.request, "You need to be a Player to create a team.")
            return HttpResponseRedirect('/players/sign-up')

            


class TeamListView(ListView):
    def get_queryset(self):
        queryset = Team.objects.all()
        return queryset

class TeamDetailView(DetailView):
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["MatchWins"] = Match.objects.all().filter(winningTeam=kwargs["object"]).count()
        context["TournamentWins"] = Bracket.objects.all().filter(winningTeam=kwargs["object"]).count()
        return context


@login_required
def join_team(request, **kwargs):
    print("join_team() called")
    print(kwargs)
    user = request.user
    player = Player.objects.get(account = user)
    print(request.META['HTTP_REFERER'])
    if player is not Player.DoesNotExist:
        print("adding player")
        print(request.META['QUERY_STRING'])
        #request.objects.players.add(player)#here
        team = Team.objects.get(slug=kwargs['slug'])
        team.players.add(player)
        return  HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect('/login/')
            

