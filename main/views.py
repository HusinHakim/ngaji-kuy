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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

@login_required(login_url='/login')
def show_main(request): 
   
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'name': request.user.username,
        'Class' : "PBP C",
        
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
    data = Quran.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Quran.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Quran.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def register(request):
    if request.method == "POST":
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # Validate password strength
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e:
                messages.error(request, error)
            return render(request, 'register.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('main:login')

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        # Get the username and password from POST data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


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


@login_required
@require_POST
def add_quran_entry_ajax(request):
    form = QuranForm(request.POST)
    if form.is_valid():
        quran_entry = form.save(commit=False)
        quran_entry.user = request.user
        quran_entry.save()
        quran_data = {
            'pk': str(quran_entry.id),
            'fields': {
                'name': quran_entry.name,
                'price': quran_entry.price,
                'description': quran_entry.description,
                'stock': quran_entry.stock,
                'publisher': quran_entry.publisher,
                'type': quran_entry.type,
            }
        }
        return JsonResponse(quran_data, status=201)
    else:
        errors = form.errors.get_json_data()
        return JsonResponse({'error': errors}, status=400)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = Quran.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description = data["description"],
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
