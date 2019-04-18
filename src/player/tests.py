from django.test import TestCase, RequestFactory
from player.models import Player
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import User
from player.forms import PlayerCreateForm, RigesterForm
from player.views import PlayerListView

# Create your tests here.
class PlayerTest(TestCase):
    #model test
    def create_Player(self):
        user = User.objects.create_user(username='testuser', password='12345')
        #login = self.client.login(username='testuser', password='12345')
        return Player.objects.create(account=user, gameName = 'testPlayer')

    def test_player_creation(self):
        p = self.create_Player()
        self.assertTrue(isinstance(p, Player))
        self.assertEqual(p.gameName, p.title)
        self.assertEqual(p.gameName, 'testPlayer')
    
    #view Test
    def test_Player_list_view(self):
        p = self.create_Player()
        url = reverse("players")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(bytes(p.title, 'utf-8'), resp.content)

    def test_Player_detail_view(self):
        p = self.create_Player()
        url = '/players/'+ p.slug + '/'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(bytes(p.title, 'utf-8'), resp.content)

    #form test
    def test_PlayerCreation_valid_form(self):
        p = self.create_Player()
        data = {'gameName': p.gameName,}
        form = PlayerCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_PlayerCreation_invalid_form(self):
        p = self.create_Player()
        data = {'gameName': '',}
        form = PlayerCreateForm(data=data)
        self.assertFalse(form.is_valid())

    def test_Rigester_valid_form(self):
        #user = User.objects.create_user(username='testuser', password='12345')
        data = {'username': 'tetername', 'password1' :'12345', 'password2':'12345',}
        form = RigesterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_Rigester_invalid_form(self):
        user = User.objects.create_user(username='testuser', password='12345')
        data = {'username': user.username, 'password1': '12345', 'password2' : '123456',}
        form = RigesterForm(data=data)
        self.assertFalse(form.is_valid())
    

    
    

    