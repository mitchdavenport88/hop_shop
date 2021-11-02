from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def_street_address = models.CharField(max_length=80, null=True, blank=True)
    def_town_or_city = models.CharField(max_length=60, null=True, blank=True)
    def_county = models.CharField(max_length=60, null=True, blank=True)
    def_postcode = models.CharField(max_length=20, null=True, blank=True)
    def_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
