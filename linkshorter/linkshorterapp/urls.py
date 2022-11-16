from django.urls import path
from . import views

app_name = "linkshorterapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_link_hash>', views.redirect_original, name='redirectoriginal'),
    path('makeshort/', views.shorten_url, name='shortenurl'),
]