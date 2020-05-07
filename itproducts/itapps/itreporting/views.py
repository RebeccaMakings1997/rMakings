from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review, Product
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse



def home(request):
    return render(request, 'itproducts/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'itproducts/about.html', {'title': 'About us'})


def contact(request):
    return render(request, 'itproducts/contact.html', {'title': 'Contact'})


def products(request):
	products = {
	'products': Product.objects.all()
	}
	return render(request, 'itproducts/products.html', products ,{'title': 'Products'})


def smartphone(request):
    return render(request, 'itproducts/smartphone.html', {'title': 'smartphones'})


def smartwatches(request):
    return render(request, 'itproducts/smartwatches.html', {'title': 'smartwatches'})


def smarttv(request):
    return render(request, 'itproducts/smarttv.html', {'title': 'smarttv'})


def review(request):
    reviews = {
    'reviews': Review.objects.all()
        }
    return render(request, 'itproducts/review.html', reviews)

class PostListView(ListView):
        model = Review
        template_name = 'itproducts/review.html'
        context_object_name = 'reviews'
        ordering = ['-date']
        paginate_by = 5

class UserPostListView(ListView):
        model = Review
        template_name = 'itproducts/user_review.html'
        context_object_name = 'reviews'
        ordering = ['-date']
        paginate_by = 5
def get_queryset(self):
	user=get_object_or_404(User, username=self.kwargs.get('username'))
	return Review.objects.filter(author=user). order_by('-date')

class PostDetailView(DetailView):
        model = Review


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'details', 'products']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'details', 'products']

    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/review'


def test_func(self):
    Review = self.get_object()
    if self.request.user == Review.author:
        return True
    return False
