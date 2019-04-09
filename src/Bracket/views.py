from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from math import ceil, sqrt, log

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


def bracket_gen(request, **kwargs):
    qs = Bracket.objects.get(slug=kwargs['slug'])
    regTeams = qs.teams.all()
    print(regTeams)
    count = regTeams.count()

    num_of_rounds = ceil(log(count, 2))
    print(num_of_rounds)

    teamNum = 0
    for round in range(num_of_rounds):
        count = count//2
        new_round = Round(num = round+1)
        new_round.save()
        if round == 0:
            for matches in range(count):
                match = Match(team1 = regTeams[teamNum], team2 = regTeams[teamNum + 1])
                match.save()
                teamNum = teamNum + 2
                new_round.matches.add(match)
        else:
            for matches in range(count):
                match = Match()
                match.save()
                new_round.matches.add(match)
        new_round.save()
        qs.rounds.add(new_round)

    qs.hasBeenGenerated = True
    qs.save()
    return  HttpResponseRedirect(request.META['HTTP_REFERER'])


def divide(arr, depth, m, complements):
    if len(complements) <= depth:
        complements.append(2 ** (depth + 2) + 1)
    complement = complements[depth]
    for i in range(2):
        if complement - arr[i] <= m:
            arr[i] = [arr[i], complement - arr[i]]
            divide(arr[i], depth + 1, m, complements)

