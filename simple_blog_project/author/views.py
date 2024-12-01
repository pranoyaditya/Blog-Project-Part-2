from django.shortcuts import render,redirect
from .forms import RegisterForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'author/register.html', {'form' : form, 'type': 'Register'})

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            userPass = form.cleaned_data['password']
            user = authenticate(username = userName, password = userPass)
            if user:
                login(request,user)
                return redirect('profile')
    return render(request, 'author/register.html', {'form' : form, 'type': 'Login'})