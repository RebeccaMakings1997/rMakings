from django.shortcuts import render
from.import views


def home(request):
    return render(request, 'itproducts/home.html')
def about(request):
   return render(request, 'itproducts/about.html',{'title': 'About us'})
def contact(request):
    return render(request, 'itproducts/contact.html')
def products(request):
    return render(request, 'itproducts/products.html')
def smartphone(request):
    return render(request, 'itproducts/smartphone.html')
def smartwatches(request):
    return render(request, 'itproducts/smartwatches.html')
def smarttv(request):
    return render(request, 'itproducts/smarttv.html')
def smarttv(request):
    return render(request, 'itproducts/smarttv.html')
def comment(request):
    return render(request, 'itproducts/comment.html')

