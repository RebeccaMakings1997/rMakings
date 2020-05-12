from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
ListView, 
DetailView, 
CreateView, 
UpdateView, 
DeleteView
)
from .models import Review, Product
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User   
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings



def home(request):
	return render(request, 'itproducts/home.html', {'title': 'Home'})


def about(request):
	return render(request, 'itproducts/about.html', {'title': 'About us'})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['name']
		sender_email = form.cleaned_data['email']
		message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
		send_mail('New Enquiry', message, sender_email, ['b6005208@my.shu.ac.uk'])

		return HttpResponse('Thanks for contacting us!')
	else:
		form = ContactForm()
	return render(request, 'itproducts/contact.html', {'form': form})


def products(request):
	products = {
	'products': Product.objects.all()
	}
	return render(request, 'itproducts/products.html', products)


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
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Review.objects.filter(author=user).order_by('-date')

class PostDetailView(DetailView):
	model = Review
	template_name = 'itproducts/review_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Review
	template_name = 'itproducts/review_form.html'#<app>/<model>_<viewtype>.html
	fields = ['rating','details','products']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review
	template_name = 'itproducts/review_form.html'#<app>/<model>_<viewtype>.html
	fields = ['rating','details','products']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review
	template_name = 'itproducts/review_confirm_delete.html'#<app>/<model>_<viewtype>.html
	success_url='/review'
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

