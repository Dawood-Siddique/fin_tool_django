from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login,
    logout
)
from django.contrib import messages

User = get_user_model()
# Create your views here.

class LoginPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-page')
        else:
            return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        
        else:
            messages.error(request, "Either Username or Password is wrong")
            return redirect('login-page')

class RegisterPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-page')
        else:
            return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Password do not match")
            return redirect('register-page')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register-page')
        
        user = User.objects.create_user(username=username, password=password)
        login(request=request, user=user)
        return redirect('home-page')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login-page')
