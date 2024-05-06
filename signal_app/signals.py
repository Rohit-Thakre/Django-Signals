from django.db.models.signals import post_save
from signal_app import models
from signal_app import models
from django.dispatch import receiver

@receiver(post_save, sender=models.Blog)
def blog_saved(sender, instance, created, **kwargs):
    print("post_save singnal initialized")
    # some active here when blog model in updated

    