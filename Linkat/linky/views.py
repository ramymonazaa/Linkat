from django.shortcuts import  render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app1.models import User
from django.contrib.auth.hashers import make_password
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def register(request):
    print("h1") 
    flag=False
    if request.method == 'POST' :
        form=CreateUserForm(request.POST)
        if not form.is_valid():
            print(form.error_messages)
            messages.error(request,"invalid data ")
            context={'flag':flag,'section':'22'}
            return render(request,'registration.html',context)
        user= User()
        password=str(request.POST.get('password1'))
        encoded_password=hash(password)
        # print("swsw")
        # print(request.POST.get('password1'))
        # print(request.POST.get('password2'))
        # print(encoded_password)
        # return redirect('login')
        if request.POST.get('password1')!=request.POST.get('password2'):
            print("11")
            messages.error(request,"confirm password don't match new password")
            context={'flag':flag,'section':'22'}
            return render(request,'registration.html',context)
        state=password_valid(request.POST.get('password1'))
        if state!="":
            messages.error(request,state)
            print("2")
            context={'flag':flag,'section':'22'}
            return render(request,'registration.html',context)
        # if User.objects.get(email=request.POST.get('email'))!=None:
        #     messages.error(request,"this email already exists")
        #     return render(request,'registration.html')
        if name_valid(request.POST.get('username'))==False:
            messages.error(request,"email isn't valid")
            print("4")
            context={'flag':flag,'section':'22'}
            return render(request,'registration.html',context)
        user.points=0
        user.num_visits=0
        user.password = hash(request.POST.get('password1'))
        user.username = request.POST.get('username')
        user.email=request.POST.get('email')
        user.save()
        form.save()
        print("success")
        return redirect('login')
    # messages.error(request,"invalid data")
    context={'flag':flag,'section':'22'}
    return render(request,'registration.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        f=False
        for user1 in User.objects.all():
            if user1.username == username:
                f=True
        if user is not None and User.objects.filter(username=user.username):
            login(request,user)
            return redirect('home')
        if f==True:
            messages.error(request,"invalid passowrd")
        else:
            messages.error(request,"username doesn't exist")
    flag=True
    context={'flag':flag,'section':'11'}
    return render(request,'registration.html',context)
def Choose_section(request,name1):
    if name1=='11':
        print(name1)
        context={'flag':True,'section':'11'}
        return render(request,'registration.html',context)
    else:
        print('name1')
        context={'flag':False,'section':'22'}
        return render(request,'registration.html',context)
def logoutPage(request):
    logout(request)
    return redirect('register')
def test(request):
    x=100
    print(x)
    return 

def Forget_password(request):
    sender="romeo33667@gmail.com"
    rec="romeo33667@gmail.com"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("romeo33667@gmail.com", "ramy336677")
    message=MIMEMultipart("alternatives")
    message["From"]=sender
    message["Subject"]='Link'
    message["To"]=rec
    text="this your password"
    textpart=MIMEText(text,'plain')
    message.attach(textpart)
    s.sendmail("romeo33667@gmail.com","romeo33667@gmail.com",message.as_string())
    s.quit()
    return redirect('register')

def hash(password):
    new=""
    for key in password:
        new+=chr(ord(key)-4)
        new+=chr(ord(key)-9)
        new+=chr(ord(key)-7)
        new+=chr(ord(key)+1)
    # print(new)
    return new

def email_valid(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,s):
        return True
    return False
def name_valid(s):
    print(s)
    for i in s:
        if i.isalpha()==False and i.isdigit():
            return False
    if len(s)>3:
        return True
    return False

def password_valid(s):
    l, u, p, d = 0, 0, 0, 0
    state=""
    if (len(s) >= 8):
        for i in s:
            # counting lowercase alphabets
            if (i.islower()):
                l+=1		

            # counting uppercase alphabets
            if (i.isupper()):
                u+=1		

            # counting digits
            if (i.isdigit()):
                d+=1		
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'or i=='&' or i=='*' or i=='#'):
                p+=1		
        if (l==0):
            state+="At least one alphabet should be of Lower Case.\n"
        if (u==0):
            state+="At least one alphabet should be of Upper Case.\n"    
        if (d==0):
            state+="At least 1 number or digit between [0-9].\n"
        if (p==0):
            state+="At least 1 character from [ _ or @ or $ or & or * or #].\n"
        if l+u+d+p!= len(s):
            state+="invalid char inserted\n"
    else:
        state+="password length must be 8 characters at least.\n"
    return state
# @login_required(login_url='login')    