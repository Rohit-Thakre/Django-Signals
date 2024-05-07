from django.contrib import admin
from signal_app import models


admin.site.register(models.Blog)
admin.site.register(models.Author_Notification)