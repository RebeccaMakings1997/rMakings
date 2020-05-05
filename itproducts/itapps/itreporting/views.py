from django.shortcuts import render
from.import views
from .models import Review
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'itproducts/home.html',{'title': 'Home'})
def about(request):
   return render(request, 'itproducts/about.html',{'title': 'About us'})
def contact(request):
    return render(request, 'itproducts/contact.html'{'title': 'Contact'})
def products(request):
    return render(request, 'itproducts/products.html'{'title': 'Products'})
def smartphone(request):
    return render(request, 'itproducts/smartphone.html'{'title': 'smartphones'})
def smartwatches(request):
    return render(request, 'itproducts/smartwatches.html'{'title': 'smartwatches'})
def smarttv(request):
    return render(request, 'itproducts/smarttv.html'{'title': 'smarttv'})
def review(request):
    reviews = {
          'reviews':Review.objects.all()
         }
    return render(request, 'itproducts/review.html',reviews)
 class PostListView(ListView):
    model = Review
    template_name= 'itproducts/review.html'
    context_object_name = 'reviews'
    ordering = ['-date']
 class PostDetailView(DetailView):
    model= Review

 



