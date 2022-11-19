from django.contrib import admin
from .models import Shorter


# Register your models here.
class ShorterAdmin(admin.ModelAdmin):
    list_display = ('short_link_hash', 'long_link', 'created', 'days_alive', 'password')
    ordering = ('-created',)


admin.site.register(Shorter, ShorterAdmin)
