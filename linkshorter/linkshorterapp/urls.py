from django.urls import path
from .views import links, single_link

urlpatterns = [
    path('', links, name='links'),
    path('links/', links, name='links'),
    path('links/<int:pk>', single_link, name='single_link')
]
