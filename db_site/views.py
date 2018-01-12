from django.shortcuts import render

from .models import Studio
# Create your views here.

def studios_list(request):
    studios = Studio.objects.all()
    return render(request, 'site/studios_list.html', {'studios':studios})
