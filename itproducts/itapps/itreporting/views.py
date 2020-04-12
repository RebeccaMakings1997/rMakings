from django.shortcuts import render

def home(request):
    return render(request, 'itreporting/home.html')
def about(request):
   return render(request, 'itreporting/about.html')
def contact(request):
    return render(request, 'itreporting/contact.html')
def products(request):
    return render(request, 'itreporting/products.html')
def smartphone(request):
    return render(request, 'itreporting/smartphone.html')
def smartwatches(request):
    return render(request, 'itreporting/smartwatches.html')
def smarttv(request):
    return render(request, 'itreporting/smarttv.html')
