from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='liked_by')

    def __str__(self) -> str:
        return f"{self.title}_{self.author}"
    

class Author_Notification(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="user who created the blog")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, help_text="blog created by the user")
    action = models.CharField(max_length=10, help_text="action performed on the blog by some user, i.e. liked or disliked")
    notification = models.CharField(max_length=100, help_text="notification content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.notification
    
    