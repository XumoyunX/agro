from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import News, Pdf, Product, Gallery, Send
from .forms import *


def login_required_decorator(f):
    return login_required(f, login_url="main:login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('main:login')







@login_required_decorator
def product_list(request):
    categories = Product.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/categories/list.html',ctx)

@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect('main:product_list')





@login_required_decorator
def new_list(request):
    new = News.objects.all()
    ctx = {
        'new':new,
        "r_active": 'active'
    }
    return render(request,'dashboard/new/list.html',ctx)

@login_required_decorator
def new_create(request):
    model = News()
    form = NewsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:new_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/new/form.html', ctx)

@login_required_decorator
def new_edit(request, pk):
    model = News.objects.get(id=pk)
    form = NewsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:new_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/new/form.html', ctx)

@login_required_decorator
def new_delete(request, pk):
    model = News.objects.get(id=pk)
    model.delete()
    return redirect('main:new_list')




@login_required_decorator
def gallery_list(request):
    gallery = Gallery.objects.all()
    ctx = {
        'gallery':gallery,
        "g_active": 'active'
    }
    return render(request,'dashboard/gallery/list.html',ctx)

@login_required_decorator
def gallery_create(request):
    model = Gallery()
    form = GalleryForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:gallery_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/gallery/form.html', ctx)

@login_required_decorator
def gallery_edit(request, pk):
    model = Gallery.objects.get(id=pk)
    form = GalleryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:gallery_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/gallery/form.html', ctx)

@login_required_decorator
def gallery_delete(request, pk):
    model = Gallery.objects.get(id=pk)
    model.delete()
    return redirect('main:gallery_list')




@login_required_decorator
def send_list(request):
    send = Send.objects.all()
    ctx = {
        'send':send,
        "s_active": 'active'
    }
    return render(request,'dashboard/send/list.html',ctx)

@login_required_decorator
def send_create(request):
    model = Send()
    form = SendForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:send_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/send/form.html', ctx)

@login_required_decorator
def send_edit(request, pk):
    model = Send.objects.get(id=pk)
    form = SendForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:send_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/send/form.html', ctx)

@login_required_decorator
def send_delete(request, pk):
    model = Send.objects.get(id=pk)
    model.delete()
    return redirect('main:send_list')









@login_required_decorator
def pdf_list(request):
    pdf = Pdf.objects.all()
    ctx = {
        'pdf':pdf,
        "p_active": 'active'
    }
    return render(request,'dashboard/pdf/list.html',ctx)

@login_required_decorator
def pdf_create(request):
    model = Pdf()
    form = PdfForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:pdf_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/pdf/form.html', ctx)

@login_required_decorator
def pdf_edit(request, pk):
    model = Pdf.objects.get(id=pk)
    form = PdfForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:pdf_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/pdf/form.html', ctx)

@login_required_decorator
def pdf_delete(request, pk):
    model = Pdf.objects.get(id=pk)
    model.delete()
    return redirect('main:pdf_list')


















