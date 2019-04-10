from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from math import ceil, sqrt, log
from django.contrib import messages

from .models import Bracket, Match, Round
from player.models import Player
from team.models import Team

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

@login_required
def bracket_gen(request, **kwargs):
    qs = Bracket.objects.get(slug=kwargs['slug'])
    regTeams = qs.teams.all()
    num_of_teams = regTeams.count()
    if num_of_teams < qs.minNumOfTeams:
        messages.error(request, 'The minimum number of teams is not meet. There needs to be at least ' + str(qs.minNumOfTeams) +' to start the tournament')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    num_of_rounds = ceil(log(num_of_teams, 2))
    num_of_matches = pow(2, num_of_rounds)
    bytes = num_of_matches - num_of_teams
    matches_round_one = (num_of_teams - bytes)//2
    num_of_matches = num_of_matches//2
    teamNum = 0
    for round in range(num_of_rounds):
        new_round = Round(num = round+1)
        new_round.save()
        temp = matches_round_one
        match_num = 0
        print(round)
        if round == 0:
            for matches in range(num_of_matches):
                if temp > 0:
                    match = Match(team1 = regTeams[teamNum], team2 = regTeams[teamNum + 1], matchNum = match_num)
                    temp = temp - 1
                    teamNum = teamNum + 2
                else:
                    match = Match( matchNum = match_num, isByeMatch = True)
                match.save()
                match_num = match_num + 1
                new_round.matches.add(match)
        elif round == 1:
            for matches in range(num_of_matches):
                if temp == 1:
                    print("here")
                    match = Match( team2 = regTeams[teamNum], matchNum = match_num)
                    teamNum = teamNum + 1
                    temp = temp - 1
                elif temp >= 2:
                    match = Match(matchNum = match_num)
                    temp = temp - 2
                else:
                    match = Match(team1 = regTeams[teamNum], team2 = regTeams[teamNum + 1], matchNum = match_num)
                    teamNum = teamNum + 2
                match.save()
                match_num = match_num + 1
                new_round.matches.add(match)
        else:
            for matches in range(num_of_matches):
                match = Match(matchNum = match_num)
                match.save()
                match_num = match_num + 1

                new_round.matches.add(match)
        num_of_matches = num_of_matches//2
        new_round.save()
        qs.rounds.add(new_round)

    qs.hasBeenGenerated = True
    qs.save()
    return  HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
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
