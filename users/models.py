
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=30, blank=True)

    photo = models.ImageField( upload_to='media/users/pictures', default= 'media/users/pictures/perfilsinfoto.png')

    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
