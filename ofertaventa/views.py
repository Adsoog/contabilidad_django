from django.shortcuts import render, HttpResponse


# Create your views here.

def ofertaventa(request):
    return render(request, "home.html")


