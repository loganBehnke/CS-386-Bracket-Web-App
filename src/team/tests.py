from django.test import TestCase
from player.models import Player
from team.models import Team
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import User
from team.forms import TeamCreateForm, JoinTeamForm
from team.views import TeamListView

# Create your tests here.
class TeamTest(TestCase):
    #Team creation
    def create_team(self):
        user = User.objects.create_user(username='testuser', password='12345')
        player = Player.objects.create(account=user, gameName = 'testPlayer')
        return Team.objects.create(name = 'testTeam', teamCaptin = player)
  
    def test_team_creation(self):
        t = self.create_team()
        self.assertTrue(isinstance(t, Team))
        self.assertEqual(t.name , 'testTeam')
        self.assertEqual(t.title , 'testTeam')

    #View test
    def test_team_list_view(self):
        t = self.create_team()
        url = reverse("teams")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes(t.title, 'utf-8'), response.content)

    def test_team_detail_view(self):
        t = self.create_team()
        url = '/teams/' + t.slug + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes(t.title, 'utf-8'), response.content)

    #TODO Join team view

    #Form test
    def test_create_team_form(self):
        t = self.create_team()
        data = {'name': t.name}
        form = TeamCreateForm(data = data)
        self.assertTrue(form.is_valid())

    def test_join_team_form(self):
            user = User.objects.create_user(username='testuser3', password='12345')
            player = Player.objects.create(account=user, gameName = 'testPlayer')
            t = self.create_team()
            data = {'players': player}
            form = JoinTeamForm(data)
            self.assertTrue(form.is_valid())