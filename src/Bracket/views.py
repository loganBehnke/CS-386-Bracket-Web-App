from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Bracket
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
