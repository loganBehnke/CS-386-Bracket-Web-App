"""BestBracketz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from Bracket.views import BracketListView, BracketDetailView, BracketCreateView, join_bracketz, bracket_gen, advance_team
from player.views import PlayerListView, PlayerDetailView, RegisterView, PlayerCreateView
from RegisteredTeams.views import TeamDetailView, TeamListView, TeamCreateView, join_team


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^teams/$', TeamListView.as_view(), name='teams'),
    url(r'^teams/sign-up/$', TeamCreateView.as_view(), name='teams-sign-up'),
    url(r'^teams/join-team/(?P<slug>[\w-]+)/$', join_team),
    url(r'^teams/(?P<slug>[\w-]+)/$', TeamDetailView.as_view()),
    url(r'^players/$', PlayerListView.as_view(), name='players'),
    url(r'^players/sign-up/$', PlayerCreateView.as_view(), name='player-sign-up'),
    url(r'^players/(?P<slug>[\w-]+)/$', PlayerDetailView.as_view()),
    url(r'^bracketz/$', BracketListView.as_view(), name='bracketz'),
    url(r'^bracketz/creation/$', BracketCreateView.as_view(), name='bracketz-creation'),
    url(r'^bracketz/(?P<slug>[\w-]+)/$', BracketDetailView.as_view()),
    url(r'^bracketz/generate/(?P<slug>[\w-]+)/$', bracket_gen),
    #url(r'^bracketz/join-bracketz/(?P<slug>[\w-]+)/$', join_bracketz), #TODO in future version
    url(r'^bracketz/advanceTeam/(?P<slug>[\w-]+)/(?P<winTeam>[\w-]+)/(?P<matchNum>[\w-]+)/(?P<roundNum>[\w-]+)/$', advance_team)

]
