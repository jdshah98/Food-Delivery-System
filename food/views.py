from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages
from django.conf import settings

# Create your views here.
app = settings.APP_NAME


def home(request):
    return render(request, 'food/home.html', {'title': 'home', 'app' : app})


def menu(request):
    return render(request, 'food/menu.html', {'title': 'menu', 'app' : app})


def about(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            if request.user.is_authenticated:
                feed.email = request.user.email
                feed.username = request.user.username
            else:
                feed.email = 'anonymous@gmail.com'
                feed.username = 'anonymous'
            form.save()
            messages.success(request,f'Your Feedback is Submitted Successfully')
            return redirect('food-about')
    else:
        form = FeedbackForm()
        return render(request, 'food/about.html', {'title': 'about', 'form': form, 'app' : app})


def cart(request):
    return render(request, 'food/cart.html', {'title': 'cart', 'app' : app})
