from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def about(request):
	return render(request, 'personal/about.html')

def portfolio(request):
	return render(request, 'personal/portfolio.html')

def contact(request):
	return render(request, 'personal/contact.html')
