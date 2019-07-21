from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RestRegisterForm, RestProfileForm
from django.contrib import messages
from .models import RestProfile

# Create your views here.
app = settings.APP_NAME

def register(request):
	if request.method == 'POST':
		form = RestRegisterForm(request.POST)
		if form.is_valid():
			rest_form = form.save(commit=False)
			rest_form.usertype = "restaurant"
			form.save()
			RestProfile.objects.create(user=instance)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created Successfully! You are now able to Log In')
			return redirect('rest-profile')
	else:
		form = RestRegisterForm()
	return render(request, 'restaurants/register.html', {'title': 'join us', 'app': app, 'form': form})

@login_required(login_url='rest-login')
def profile(request):
	if request.method == 'POST':
		p_form = RestProfileForm(request.POST, request.FILES,
		                         instance=request.user.profile)
		if p_form.is_valid():
			p_form.save()
			messages.success(request, f'Your Profile has been Updated Successfully!')
			return redirect('rest-profile')
	else:
		p_form = RestProfileForm(instance=request.user.profile)
	return render(request, 'restaurants/profile.html', {'title': 'profile', 'app': app, 'form': p_form})

def login(request):
	return render(request, 'restaurants/login.html', {'title': 'login', 'app': app})

def logout(request):
	return render(request, 'restaurants/logout.html', {'title': 'logout', 'app': app})