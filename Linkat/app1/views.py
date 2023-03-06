from django.shortcuts import render,HttpResponse,redirect
from .models import Category,Product
from .models import User as us
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import re

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
# Create your views here.
signed="F"
class pr:
    name=""
    email=""
    description=""
    rate=0
    category=""
    state=0
section="profile"
print(signed)
def Add_fave(request):
    return home(request); 
def Add_fav(request,name1):
    product=Product.objects.get(name=name1)
    user=us.objects.get(username=request.user)
    # print("#")
    # for pr in user.fav_products.all():
    #       print (pr.name)
    user.fav_products.add(product)
    user.save()
    # print("#")
    # for pr in user.fav_products.all():
    #       print (pr.name)
    return home(request); 
def Del_fav(request,name1):
    product=Product.objects.get(name=name1)
    user=us.objects.get(username=request.user)
    user.fav_products.remove(product)
    user.save()
    return home(request); 
def search(request):
    if request.method == 'POST':
        search =""
        if request.POST.get('search'):
            search= request.POST.get('search')
        else:
            search =""
            # print('ssssssssssssssss')
        found ="T"
        products1=[]
        categories=Category.objects.all()
        mx=1
        for product in Product.objects.all():
            if product.rate>mx:
                mx=product.rate
            if product.state!=1:
                continue
            if str(product.category).lower().find(search.lower())!=-1 or str(product.name).lower().find(search.lower())!=-1: 
                products1.append(product)
        if len(products1)==0:
            found="F"
        products_S=[]
        for product in products1:
            pr1=pr()
            pr1.category=str(product.category)
            pr1.name=product.name
            pr1.description=product.description
            pr1.rate=int(float("{:.0f}".format((product.rate/mx)*100)))
            pr1.email=product.email
            
            products_S.append(pr1)
        products1=Product.objects.all()
        products=[]
        for product in products1:
            if product.state!=1:
                continue
            pr1=pr()
            pr1.category=str(product.category)
            pr1.name=product.name
            pr1.description=product.description
            pr1.rate=int(float("{:.0f}".format((product.rate/mx)*100)))
            pr1.email=product.email
            products.append(pr1)
        categories=Category.objects.all()
        return render(request, 'searchResult.html',{'dash_products':products,'products':products_S,'categories':categories,'found':found,'signed':signed})
def home(request):
    products1=Product.objects.all()
    products=[]
    mx=1
    for product in products1:
        pr1=pr()
        if product.rate>mx:
            mx=product.rate
    for product in products1:
        pr1=pr()
        if product.state!=1:
                continue
        pr1.category=str(product.category)
        pr1.name=product.name
        pr1.description=product.description
        pr1.rate=int(float("{:.0f}".format((product.rate/mx)*100)))
        pr1.email=product.email
        products.append(pr1)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories,'signed':signed})
def profile(request, section="11"):
    # print("section "+section)
    products1=Product.objects.all()
    products=[]
    for product in products1:
        if str(product.owner)!= str(request.user):
            continue
        pr1=pr()
        pr1.category=str(product.category)
        pr1.name=product.name
        pr1.description=product.description
        pr1.rate=product.rate
        pr1.email=product.email
        pr1.state=product.state
        products.append(pr1)
    categories=Category.objects.all()
    user=us.objects.get(username=request.user)
    index=1
    for user1 in us.objects.all():
        # print(user1.points)
        if user1==user:
            break;
        index=index+1
    # print(index)
    # print(len(user.fav_products.all()))
    return render(request, 'profile.html',{'section':section,'fav':user.fav_products.all(),'user':user,'index':index,'products':products,'categories':categories})

def visit_action(request,name1):
    product=Product.objects.get(name=name1)
    product.rate=product.rate+1
    link_address=product.email
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        user=us.objects.get(username=request.user)
        user.points=user.points+2
        user.num_visits=user.num_visits+1
        # user.fav_products.add(product)  
        user.save()
    product.save()
    return redirect(link_address);

def category_home_page(request,id_):
    products=[]
    for product in Product.objects.all():
        if product.state!=1:
                continue
        if str(product.category).lower()==id_.lower(): 
            products.append(product)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})
def Add_article(request):
    if request.method == 'POST':
        # if Product.objects.get(name=request.POST.get('name')):
        # print("sssssssssss")
        # print(len(request.POST.get('state')))
        if request.POST.get('state')!="":
            product=Product.objects.get(name=request.POST.get('state'))
            product.delete()
            
        for product in Product.objects.all():
            if product.name == request.POST.get('name'):
                messages.error(request,"name already exists")
                return home(request)
                
        product = Product()
        cat=Category.objects.get(name=request.POST.get('category'))
        product.category=cat
        product.name=request.POST.get('name')
        product.email=request.POST.get('url')
        product.state=2
        product.owner=request.user
        print(request.POST.get('description'))
        print(request.POST.get('category'))
        product.save()
        # 
    return profile(request,"33");
    
def Delete_item(request,name):
    # Product.objects.filter(name=name).delete()
    product=Product.objects.get(name=name)
    print(product)
    product.delete()
    return profile(request,"33");

def Change_section(request,name1):
    # Product.objects.filter(name=name).delete()
    print(name1);
    return profile(request,name1);
def View_item(request,search):
    found ="T"
    products1=[]
    categories=Category.objects.all()
    mx=1
    for product in Product.objects.all():
        if product.rate>mx:
            mx=product.rate
        if product.state!=1:
            continue
        if str(product.category).lower().find(search.lower())!=-1 or str(product.name).lower().find(search.lower())!=-1: 
            products1.append(product)
    if len(products1)==0:
        found="F"
    products_S=[]
    for product in products1:
        pr1=pr()
        pr1.category=str(product.category)
        pr1.name=product.name
        pr1.description=product.description
        pr1.rate=int(float("{:.0f}".format((product.rate/mx)*100)))
        pr1.email=product.email
        
        products_S.append(pr1)
    products1=Product.objects.all()
    products=[]
    for product in products1:
        if product.state!=1:
            continue
        pr1=pr()
        pr1.category=str(product.category)
        pr1.name=product.name
        pr1.description=product.description
        pr1.rate=int(float("{:.0f}".format((product.rate/mx)*100)))
        pr1.email=product.email
        products.append(pr1)
    categories=Category.objects.all()
    return render(request, 'searchResult.html',{'dash_products':products,'products':products_S,'categories':categories,'found':found,'signed':signed})
def Update_user_info(request):
    print(request.method)
    if request.method == 'POST':
        user=us.objects.get(username=request.user)
        password=str(request.POST.get('old_password'))
        encoded_password=hash(password)
        
        print(password)
        print(encoded_password)
        print(user.password)
        if str(encoded_password)!=str(user.password):
            # print(encoded_password)
            # print(user.password)
            messages.error(request,"password isn't correct")
            return profile(request,"44")
        if request.POST.get('password1')!=request.POST.get('password2'):
            messages.error(request,"confirm password don't match new password")
            return profile(request,"44")
        state=password_valid(request.POST.get('password1'))
        if state!="":
            messages.error(request,state)
            return profile(request,"44")
        if us.objects.get(email=request.POST.get('email'))!=None and user.email!=request.POST.get('email'):
            messages.error(request,"this email already exists")
            return profile(request,"44")
        if email_valid(request.POST.get('email'))==False:
            messages.error(request,"email isn't valid")
            return profile(request,"44")
        if name_valid(request.POST.get('name'))==False:
            messages.error(request,"name isn't valid")
            return profile(request,"44")
        user.password = hash(request.POST.get('password1'))
        user.username = request.POST.get('name')
        user.email=request.POST.get('email')
        user.save()
        return profile(request,"44")
    return profile(request,"44")

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
    for i in s:
        if i.isalpha()==False and i.isdigit():
            return False
    if len(s)>=3:
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
