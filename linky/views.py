from django.shortcuts import  render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.models import User
def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user= User()
            user.username=form.cleaned_data["username"]
            user.password=form.cleaned_data["password1"]
            user.email=form.cleaned_data["email"]
            user.points=0
            user.num_visits=0
            user.save()
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account wa created for '+ user)
            return redirect('login')
    context={'form': form}
    return render(request,'registration.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context={}
    return render(request,'registration.html',context)

def logoutPage(request):
    logout(request)
    return redirect('register')

# @login_required(login_url='login')    