from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(max_length=50)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserProfileForm(forms.ModelForm):
	firstname = forms.CharField(max_length=20, required=False)
	lastname = forms.CharField(max_length=20, required=False)
	mobile = forms.CharField(max_length=13, required=False)
	image = forms.ImageField()

	class Meta:
		model = Profile
		fields = ['firstname','lastname','mobile','image']

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['image'].required = False


class UserUpdateForm(forms.ModelForm):
	username = forms.CharField(max_length=50, required=False)
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username','email']