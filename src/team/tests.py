from django.test import TestCase
from team.models import Team
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import User
from player.forms import TeamCreateForm, JoinTeamForm
from player.views import TeamListView

# Create your tests here.
class TeamTest(TestCase):
    #Team creation
    def create_team(self):
        return Team.objects.create_team(name = 'testTeam')
  
    def test_team_creation(self):
        t = self.create_team()
        self.assertTrue(isinstance(t, Team))
        self.assertEqual(t.name, 'testTeam')
        
