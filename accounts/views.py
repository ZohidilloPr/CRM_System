from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import RegisterUser
from .models import User
# Create your views here.

class RegisterCreateView(CreateView):
    model = User
    form_class = RegisterUser
    template_name = 'register/register.html'
    success_url = '/'


def LogIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('List:Home')
    form = AuthenticationForm
    return render(request, 'register/login.html', context={'form':form})