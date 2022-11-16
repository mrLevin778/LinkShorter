from django.db import models


class Shorter(models.Model):
    long_link = models.URLField(max_length=500)
    short_link_hash = models.SlugField(max_length=7, primary_key=True)
    password = models.CharField(max_length=128)
    days_alive = models.IntegerField(default=90)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_link
