from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings

from dreamer.forms import ContactFrom, QuoteFrom, ReviewFrom

from dreamer.models import Review
from django.core.mail import BadHeaderError, send_mail


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
        forms = QuoteFrom(request.POST)
        if forms.is_valid():
            form = forms.save()
            subject = form.full_name + ' Requested for Quotes'
            from_mail = settings.EMAIL_HOST_USER
            to_mail = form.email
            body = """
                name: {name}
                email: {email}
                phone: {phone}
                heard by: {hear_about_us}
                amount of item: {amount}
                is_elevator: {elevator}
                zip code moving from: {from_zip}
                zip code moving to: {from_to}
                floor: {floor}
                square footage {square}


            """.format(
                    name=form.full_name,
                    email=form.email,
                    phone=form.phone,
                    hear_about_us=form.hear_about_us,
                    amount=form.amount,
                    elevator=form.is_elevator,
                    from_zip=form.from_zip,
                    from_to=form.from_zip,
                    floor=form.floor,
                    square=form.square_footage
            )
            # try:
            #     send_mail(
            #         subject,
            #         body,
            #         settings.EMAIL_HOST_USER, # From mail
            #         [form.email], #to mail
            #     )
            # except BadHeaderError:
            #     return HttpResponse("Your request is faild")

            messages.success(request, 'We have received your request, we will back to you shortly!', extra_tags='alert alert-success')
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