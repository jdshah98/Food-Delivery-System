from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class RestRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RestProfileForm(forms.ModelForm):
    restaurant_name = forms.CharField(max_length=20, required=False)
    manager_name = forms.CharField(max_length=20, required=False)
    phone = forms.CharField(max_length=13, required=False)
    mobile = forms.CharField(max_length=13, required=False)
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['restaurant_name', 'manager_name', 'phone', 'mobile', 'image']

    def __init__(self, *args, **kwargs):
        super(RestProfileForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class RestFoodForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    description = forms.CharField(max_length=255,required=True)
    category = forms.CharField(max_length=30, required=True)
    cost = forms.CharField(max_length=10, required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = Profile
        fields = ['name', 'description', 'category', 'cost', 'image']
