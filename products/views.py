from django.shortcuts import render
from .models import Categories,Brands,Products,Tags

def index(request):
    products = Products.objects.filter(home=True)
    return render(request, "index.html", {
        "products": products
    })

def about(request):
    return render(request, "about.html")