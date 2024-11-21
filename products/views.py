from django.shortcuts import render, get_object_or_404
from .models import Categories,Brands,Products,Tags

def index(request):
    products = Products.objects.filter(home=True)
    return render(request, "index.html", {
        "products": products
    })

def about(request):
    return render(request, "about.html")

def product_detail(request, slug):
    product =get_object_or_404(Products,slug=slug)
    return render(request, "product.html", {
        "product": product
    })