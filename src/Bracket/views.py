from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from Bracket.models import Bracket

# Create your views here.
class BracketListView(ListView):
    def get_queryset(self):
        queryset = Bracket.objects.all()
        return queryset

class BracketDetailView(DetailView):
    queryset = Bracket.objects.all()