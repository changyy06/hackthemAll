from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from forms import RegisterForm, LoginForm

def home(request):
    return render(request, 'mysite/home.html')

def about(request):
    return render(request, 'mysite/about.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home or another page
    else:
        form = RegisterForm()
    return render(request, 'mysite/register.html', {'form': form})      

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
            
    else:
        form = LoginForm()
    return render(request, 'mysite/login.html', {'form': form})



