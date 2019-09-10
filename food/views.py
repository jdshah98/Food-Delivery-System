from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages
from django.conf import settings
from django.views.generic import ListView
from .models import Food

# Create your views here.
app = settings.APP_NAME


def home(request):
    return render(request, 'food/home.html', {'title': 'home', 'app' : app})


class MenuView(ListView):
    model = Food
    template_name = 'food/menu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'title': 'Menu', 'app': app, 'foods': Food.objects.all()}


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
        return render(request, 'food/about.html', {'title': 'about', 'form': form, 'app': app})


def cart(request):
    return render(request, 'food/cart.html', {'title': 'cart', 'app' : app})
