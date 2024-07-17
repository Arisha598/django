from django.shortcuts import render

def swag(request):
    return render(request, "main/swag.html")

def swagme2(request):
    return render(request, "main/swagme.html")

def swagmeandyou3(request):
    return render(request, "main/swagmeandyou.html")