from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RestRegisterForm, RestProfileForm
from django.contrib import messages
from food.forms import FeedbackForm
from users.models import UserType
from django.contrib.auth.models import User
from food.models import Food
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

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


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['name', 'description', 'category', 'cost', 'image']
    template_name = 'restaurants/food_form.html'

    def get_success_url(self):
        return reverse('rest-list')

    def form_valid(self, form):
        form.instance.restaurant = self.request.user
        return super().form_valid(form)


class FoodListView(ListView):
    model = Food
    template_name = 'restaurants/food_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'title': 'Your Menu List', 'app': app, 'foods': Food.objects.filter(restaurant=self.request.user)}


class FoodDetailView(DetailView):
    model = Food
    template_name = 'restaurants/food_detail.html'


class FoodUpdateView(UpdateView, UserPassesTestMixin):
    model = Food
    fields = ['name', 'description', 'category', 'cost', 'image']
    template_name = 'restaurants/food_update.html'

    def get_success_url(self):
        return reverse('rest-list')

    def form_valid(self, form):
        form.instance.restaurant = self.request.user
        return super().form_valid(form)

    def test_func(self):
        food = self.get_object()
        if self.request.user == food.restaurant:
            return True
        return False


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'restaurants/food_delete.html'

    def get_success_url(self):
        return reverse('rest-list')

    def test_func(self):
        food = self.get_object()
        if self.request.user == food.restaurant:
            return True
        return False
