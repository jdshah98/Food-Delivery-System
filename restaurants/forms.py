from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import RestProfile
from users.models import User

class RestRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class RestProfileForm(forms.ModelForm):

	class Meta:
		model = RestProfile
		fields = ['restaurantname','managername','phone','address','image']

	def __init__(self, *args, **kwargs):
		super(RestProfileForm, self).__init__(*args, **kwargs)
		self.fields['image'].required = False

class RestLoginForm(AuthenticationForm):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50 , widget=forms.PasswordInput())
	
	def __init__(self, *args, **kwargs):
		super(RestLoginForm, self).__init__(*args, **kwargs)
		self.arg = arg