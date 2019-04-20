from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from player.models import Player
from django.contrib.auth.admin import User
from team.models import Team
from Bracket.models import Bracket, Match, Round
from Bracket.forms import BracketCreateForm, JoinBracketForm


# Create your tests here.
class BracketTest(TestCase):
    
    #model test
    def create_Match(self):
        user1 = User.objects.create_user(username='testuser1', password='12345')
        player1 = Player.objects.create(account=user1, gameName = 'testPlayer1')
        team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
        user2 = User.objects.create_user(username='testuser2', password='12345')
        player2 = Player.objects.create(account=user2, gameName = 'testPlayer2')
        team2 = Team.objects.create(name = 'testTeam2', teamCaptin = player2)
        return Match.objects.create(team1 = team1, team2= team2)

    def create_Round(self):
        match = self.create_Match()
        round1 = Round.objects.create(num = 1)
        round1.save()
        round1.matches.add(match)
        round1.save()
        return round1

    def create_Bracket(self):
        user = User.objects.create_user(username='testuser', password='12345')
        player1 = Player.objects.create(account=user, gameName = 'testPlayer1')
        team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
        round1 = self.create_Round()
        bracket = Bracket.objects.create(name = 'TestBracket', minNumOfTeams = 1, hasBeenGenerated = False)
        bracket.save()
        bracket.rounds.add(round1)
        bracket.teams.add(team1)
        bracket.save()
        return bracket;       

    def test_match_creation(self):
        m = self.create_Match()
        self.assertTrue(isinstance(m, Match))

    def test_round_creation(self):
        r = self.create_Round()
        self.assertTrue(isinstance(r, Round))
        self.assertIn(r.title, "Round 1")
    
    def test_bracket_creation(self):
        b = self.create_Bracket()
        self.assertTrue(isinstance(b, Bracket))
        self.assertEqual(b.title, "TestBracket")
        self.assertEqual(b.minNumOfTeams, 1)
        self.assertEqual(b.hasBeenGenerated, False)
    
    #view Test
    def test_Bracket_list_view(self):
        b = self.create_Bracket()
        url = reverse("bracketz")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(bytes(b.title, 'utf-8'), resp.content)

    def test_Bracket_detail_view(self):
        b = self.create_Bracket()
        url = '/bracketz/'+ b.slug + '/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(bytes(b.title, 'utf-8'), resp.content)

    #form test
    def test_BracketCreation_valid_form(self):
        user3 = User.objects.create_user(username='testuser3', password='12345')
        user3.save()
        login = self.client.login(username='testuser3', password='12345')
        player1 = Player.objects.create(account=user3, gameName = 'testPlayer1')
        team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
        data = {'name': 'testBracket', 'minNumOfTeams': 1, 'teams': [team1]}
        form = BracketCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_BracketCreation_invalid_form(self):
       user4 = User.objects.create_user(username='testuser4', password='12345')
       player1 = Player.objects.create(account=user4, gameName = 'testPlayer1')
       team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
       data = {'name': '', 'minNumOfTeams': 1, 'teams': [team1]}
       form = BracketCreateForm(data=data)
       self.assertFalse(form.is_valid())

    def test_JoinBracketForm_valid_form(self):
       user5 = User.objects.create_user(username='testuser5', password='12345')
       player1 = Player.objects.create(account=user5, gameName = 'testPlayer1')
       team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
       data = {'teams': [team1]}
       form = JoinBracketForm(data=data)
       self.assertTrue(form.is_valid())

    def test_JoinBracketForm_invalid_form(self):
       user6 = User.objects.create_user(username='testuser6', password='12345')
       player1 = Player.objects.create(account=user6, gameName = 'testPlayer1')
       team1= Team.objects.create(name = 'testTeam1', teamCaptin = player1)
       data = {'teams': team1}
       form = JoinBracketForm(data=data)
       self.assertFalse(form.is_valid())
