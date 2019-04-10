from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class Player(models.Model):
    account = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=False, null=True)
    gameName = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, null=True)


    def __str__(self):
        return self.gameName

    def get_absolute_url(self):
        #return f"teams/{self.slug}"
        return reverse('players', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.gameName

def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    print("saving...")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
def rl_post_save_reciever(sender, instance, *args, **kwargs):
    print("saved")


pre_save.connect(rl_pre_save_reciever, sender=Player)

post_save.connect(rl_post_save_reciever, sender=Player)