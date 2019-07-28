from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RestRegisterForm, RestProfileForm, RestFoodForm
from django.contrib import messages
from food.forms import FeedbackForm
from users.models import UserType
from django.contrib.auth.models import User

# Create your views here.
app = settings.APP_NAME


def home(request):
    return render(request, 'restaurants/home.html', {'title': 'home', 'app': app})


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
            messages.success(request, f'Your Feedback is Submitted Successfully')
            return redirect('rest-about')
    else:
        form = FeedbackForm()
        return render(request, 'restaurants/about.html', {'title': 'about', 'form': form, 'app' : app})


def register(request):
    if request.method == 'POST':
        form = RestRegisterForm(request.POST)
        if form.is_valid():
            print("hello1")
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            UserType.objects.create(user=user, user_type="restaurant")
            user.usertype.save()
            print("hello2")
            messages.success(request, f'Your Account has been created Successfully! You are now able to Log In')
            return redirect('rest-login')
    else:
        form = RestRegisterForm()
    return render(request, 'restaurants/register.html', {'title': 'join us', 'app': app, 'form': form})


def profile(request):
    if request.method == 'POST':
        p_form = RestProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your Profile has been Updated Successfully!')
            return redirect('rest-profile')
    else:
        p_form = RestProfileForm(instance=request.user.profile)
    return render(request, 'restaurants/profile.html', {'title': 'profile', 'app': app, 'form': p_form})


def food_create(request):
    if request.method == 'POST':
        food_form = RestFoodForm(request.POST, request.FILES, instance=request.food)
        if food_form.is_valid():
            food_form.save()
            messages.success(request, f'Your Profile has been Updated Successfully!')
            return redirect('rest-add')
    else:
        food_form = RestFoodForm(instance=request.food)
    return render(request, 'restaurants/food_form.html', {'title': 'profile', 'app': app, 'form': food_form})
