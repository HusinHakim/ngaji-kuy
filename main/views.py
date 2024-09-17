from django.shortcuts import render, redirect
from main.forms import QuranForm
from main.models import Quran
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    quran_entries = Quran.objects.all()
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'Name' : "Husin Hidayatul Hakim",
        'Class' : "PBP C",
        'quran_entries': quran_entries
    }

    return render(request, "main.html", context)

def create_quran_entry(request):
    form = QuranForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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