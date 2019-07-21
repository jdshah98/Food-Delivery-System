from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages

# Create your views here.
app = settings.APP_NAME

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your Account has been created Successfully! You are now able to Log In')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'title': 'sign up', 'app': app, 'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		p_form = UserProfileForm(request.POST, request.FILES, instance = request.user.profile)
		if p_form.is_valid():
			p_form.save()
			messages.success(request,f'Your Profile has been Updated Successfully!')
			return redirect('profile')
	else:
		p_form = UserProfileForm(instance=request.user.profile)
	return render(request, 'users/profile.html', {'title': 'profile', 'app' : app,'form': p_form})