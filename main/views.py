from django.conf import settings
from django.shortcuts import render

from main.forms import Sendd
from main.models import Product, News, Gallery, Send
from django.core.mail import send_mail


def home(request):
    nows = News.objects.order_by("-id")[:3]

    tex = {
        "nows": nows
    }

    return render(request, 'main/index.html', tex)


def about(request):
    return render(request, 'main/about.html')


def servicer(request):
    pro = Product.objects.all()

    ctx = {
        "pro": pro
    }
    return render(request, 'main/services.html', ctx)


def gallery(request):
    gel = Gallery.objects.all()

    ctx = {
        "gel": gel
    }
    return render(request, 'main/gallery.html', ctx)


def contact(request):
    model = Send()
    form = Sendd(request.POST,instance=model)
    if request.POST:
        if form.is_valid():
            data = request.POST
            form.save()
            message = f"Xabar keldi:\nIsmi: {data['full']}\nEmail: {data['email']}\nMavzu: {data['subject']}\nXabar: {data['message']}"
            subject = 'Saytdan'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['cool.hojimurod2001@mail.ru', 'xumoyuntoxtayev19@gmail.com']
            send_mail(subject, message, email_from, recipient_list)


    return render(request, 'main/contact.html',{"form":form})


def news(request):
    nows = News.objects.all()

    tex = {
        "nows": nows
    }

    return render(request, 'main/news.html', tex)
