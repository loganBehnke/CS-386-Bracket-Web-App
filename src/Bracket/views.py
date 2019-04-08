from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from math import ceil, sqrt, log

from .models import Bracket, Match, Round
from player.models import Player
from RegisteredTeams.models import Team

from .forms import BracketCreateForm, JoinBracketForm

# Create your views here.
class BracketListView(ListView):
    def get_queryset(self):
        queryset = Bracket.objects.all()
        return queryset

class BracketDetailView(DetailView):
    queryset = Bracket.objects.all()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class BracketCreateView(LoginRequiredMixin, CreateView):
    form_class = BracketCreateForm
    template_name = 'Bracket/form.html'
    success_url = '/bracketz/'


#TODO in future verison
@login_required
def join_bracketz(request, **kwargs):
    print("Joining Bracket")


def bracket_gen(request, **kwargs):
    qs = Bracket.objects.get(slug=kwargs['slug'])
    regTeams = qs.teams.all()
    print(regTeams)
    count = regTeams.count()

    num_of_rounds = ceil(log(count, 2))
    print(num_of_rounds)

    teamNum = 0
    for round in range(num_of_rounds):
        if count %2 == 0:
            count = count//2
        else:
            count = (count//2) +1
        new_round = Round(num = round+1)
        new_round.save()
        match_num = 0
        if round == 0:
            for matches in range(count):
                if matches == count - 1 and count % 2 != 0:
                    match = Match(team1 = regTeams[teamNum], matchNum = match_num)
                else:
                    match = Match(team1 = regTeams[teamNum], team2 = regTeams[teamNum + 1], matchNum = match_num)
                match.save()
                teamNum = teamNum + 2
                match_num = match_num + 1
                new_round.matches.add(match)
        else:
            for matches in range(count):
                match = Match(matchNum = match_num)
                match.save()
                match_num = match_num + 1
                new_round.matches.add(match)

        new_round.save()
        qs.rounds.add(new_round)

    qs.hasBeenGenerated = True
    qs.save()
    return  HttpResponseRedirect(request.META['HTTP_REFERER'])


def advance_team(request, **kwargs):
    bracket = Bracket.objects.get(slug=kwargs['slug'])
    roundFind = int(kwargs['roundNum'])
    match_num = int(kwargs['matchNum'])
    winTeam = Team.objects.get(slug=kwargs['winTeam'])
    rounds = bracket.rounds.all()
    totalNumRounds = rounds.count()
    print(totalNumRounds)
    print(roundFind)
    if totalNumRounds == roundFind:
        bracket.winningTeam = winTeam
    for round in rounds:
        if round.num == roundFind:
            for match in round.matches.all():
                if match.matchNum == match_num:
                    match.winningTeam = winTeam
                    match.save()
        elif round.num == roundFind + 1:
            for match in round.matches.all():
                if match.matchNum == match_num//2:
                    if match_num % 2 == 0:
                        match.team1 = winTeam
                    else:
                        match.team2 = winTeam
                    match.save()
        round.save()
    bracket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
