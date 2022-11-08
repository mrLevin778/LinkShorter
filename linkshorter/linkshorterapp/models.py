from django.db import models

class Shorter(models.Model):
    long_link = models.CharField(max_length=200, null=False, help_text="Copy here your loooong link")
    short_link = models.CharField(max_length=30)
    days_alive = models.IntegerField(max_length=3)
    slug = models.SlugField(max_length=7, auto_created=True)
    is_expired = models.BooleanField(default=False)
