from django.db.models.signals import post_save, m2m_changed
from signal_app import models

from django.dispatch import receiver

@receiver(m2m_changed, sender=models.Blog.liked_by.through)
def block_liked_by_updated_receiver(sender, instance,action, **kwargs):
    if action == "post_add":
        user_action = "liked"
    else: 
        user_action = "unliked"

    models.Author_Notification.objects.update_or_create(
        user= instance.author,
        blog_id = instance.id,
        defaults={"action": action,
                  "notification": 
                  f"{instance.author.username} {user_action} your blog at {instance.updated_at}"})
    

  
@receiver(post_save, sender=models.Blog)
def blog_post_save_receiver(sender, instance, created, **kwargs):
    print("blog post save receiver")