from django.shortcuts import render
from .models import Product

# def moviescoll(request):
#     return render(request, 'post2/hotmovies.html')


def moviescoll(request):
    products = Product.objects.all()
    return render(request, 'post2/hotmovies.html', {'products': products})


