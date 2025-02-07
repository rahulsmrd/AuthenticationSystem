from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
@login_required
def HomeView(request):
    return render(request, 'home/home.html')
@login_required
def ProfileView(request):
    return render(request, 'home/profile.html', {'user': request.user})

class CustomLoginView(LoginView):
    template_name = 'home/login.html'

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'home/logout.html'
@login_required
def ChangePasswordView(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home:login'))
    return render(request, 'home/change_password.html', {'user': request.user, 'form':form})

def SignUpView(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        form = UserCreationForm(data=request.POST)
        if get_user_model().objects.filter(email=email).exists():
            return render(request, 'home/signup.html', {'form': form, 'error': 'Email already exists'})
        if form.is_valid():
            get_user_model().objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=email,
            )
            return redirect(reverse_lazy('home:login'))
        return render(request, 'home/signup.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})
