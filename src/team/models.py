from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

from player.models import Player

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, null=True)

    teamCaptin = models.ForeignKey(Player, related_name='+', on_delete=models.CASCADE, blank=False, null=True)
    
    players = models.ManyToManyField(Player, related_name='players_set', blank=True)
    subs = models.ManyToManyField(Player, related_name='subs_set', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f"teams/{self.slug}"
        return reverse('teams', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name
    
def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    #print("saving...")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
#def rl_post_save_reciever(sender, instance, *args, **kwargs):
    #print("saved")


pre_save.connect(rl_pre_save_reciever, sender=Team)

#post_save.connect(rl_post_save_reciever, sender=Team)