from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

from RegisteredTeams.models import Team


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='+')
    team2 = models.ForeignKey(Team, related_name='+')

class Round(models.Model):
    matches = models.ManyToManyField(Match, blank=True)
    num = models.IntegerField(null=True, blank=True)

class Bracket(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    minNumOfTeams = models.IntegerField(null=False, blank=True, default=4)
    rounds = models.ManyToManyField(Round, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f"teams/{self.slug}"
        return reverse('bracketz', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    print("saving...")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
def rl_post_save_reciever(sender, instance, *args, **kwargs):
    print("saved")


pre_save.connect(rl_pre_save_reciever, sender=Team)

post_save.connect(rl_post_save_reciever, sender=Team)
    
 