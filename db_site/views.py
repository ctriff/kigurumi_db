from django.shortcuts import render, get_object_or_404

from .models import Studio
# Create your views here.

def studios_list(request):
    studios = Studio.objects.all().order_by('name')
    return render(request, 'site/studios_list.html', {'studios':studios})

def get_studio(request, pk):
    studio = get_object_or_404(Studio, pk=pk)
    return render(request, 'site/studio_detail.html', {'studio':studio})
