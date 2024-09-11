from django.shortcuts import render

def show_main(request):
    context = {
        'Nama_Aplikasi' : "Ngaji Kuy",
        'Name' : "Husin Hidayatul Hakim",
        'Class' : "PBP C",
    }

    return render(request, "main.html", context)