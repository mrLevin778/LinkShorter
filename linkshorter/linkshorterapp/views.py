from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Shorter

def links(request):
    links_list = Shorter.objects.all()
    data = {
        'links': list(links_list.values(
            'long_link',
            'short_link_hash',
            'password',
            'days_alive',
            'created',
            'is_active'
        ))
    }
    return JsonResponse(data)

def single_link(request, pk):
    link = get_object_or_404(Shorter, pk=pk)
    data = {
        'long_link': link.long_link,
        'short_link_hash': link.short_link_hash,
        'password': link.password,
        'days_alive': link.days_alive,
        'created': link.created,
        'is_active': link.is_active
    }
    return JsonResponse(data)
