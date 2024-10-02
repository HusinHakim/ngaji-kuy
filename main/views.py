from django.shortcuts import render, redirect, reverse
from main.forms import QuranForm
from main.models import Quran
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request): 
    quran_entries = Quran.objects.filter(user=request.user)
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'name': request.user.username,
        'Class' : "PBP C",
        'quran_entries': quran_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_quran_entry(request):
    form = QuranForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        quran_entry = form.save(commit=False)
        quran_entry.user = request.user
        quran_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_quran_entry.html", context)

def show_xml(request):
    data = Quran.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Quran.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Quran.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Quran.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_quran(request, id):
    # Get quran entry berdasarkan id
    quran = Quran.objects.get(pk = id)

    # Set quran entry sebagai instance dari form
    form = QuranForm(request.POST or None, instance=quran)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_quran.html", context)

def delete_quran(request, id):
    # Get quran berdasarkan id
    quran = Quran.objects.get(pk = id)
    # Hapus quran
    quran.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))