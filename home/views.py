from django.shortcuts import render
from dreamer.models import Review

def home(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'index.html', context=context)