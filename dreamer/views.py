from django.shortcuts import render, redirect
from django.contrib import messages

from dreamer.forms import ContactFrom, QuoteFrom, ReviewFrom

from dreamer.models import Review

def apprtment(request):
    return render(request, 'apartment.html')


def about(request):
    return render(request, 'about.html')


def review(request):
    if request.method == 'POST':
        form = ReviewFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review is published successfully!', extra_tags='alert alert-success')
        else:
            messages.error(request, 'Ooops ! an error occured', extra_tags='alert alert-danger')
    
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'review.html', context=context)


def storage(request):
    return render(request, 'storage.html')


def contact(request):
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your have received your request, we will back to you shortly!', extra_tags='alert alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Oopps ! an error occured, please try again', extra_tags='alert alert-danger')
    return render(request, 'contact.html')

def quote(request):
    if request.method == 'POST':
        form = QuoteFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your have received your request, we will back to you shortly!', extra_tags='alert alert-success')
            return redirect('home')
        else:
            messages.error(request, 'Oopps ! an error occured, please try again', extra_tags='alert alert-danger')
        
    return render(request, 'quote.html')


def office_movi(request):
    return render(request, 'office-movi.html')


def packing(request):
    return render(request, 'packing.html')

def services(request):
    return render(request, 'services.html')