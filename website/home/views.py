from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, "home.html")
# Create your views here.
def user_login(request):
    if request.method =='POST':
        print(request)
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect(home_view)
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request,'login.html',{"form":form})

def user_signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect(home_view)  # Redirect to dashboard or home page
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect(user_login)


    
    
