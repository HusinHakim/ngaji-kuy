from django.shortcuts import render

def show_main(request):
    context = {
        'name' : "Al-Qur'an Tajwid dan Terjemahan",
        'price' : "300",
        'description' : "Al-Qur'an dengan tajwid berwarna dan terjemahan lengkap.",
    }

    return render(request, "main.html", context)