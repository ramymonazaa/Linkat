from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from .models import Category,Product,User
# Create your views here.
signed="F"
class pr:
    name=""
    email=""
    description=""
    rate=0
    category=""
print(signed)
def search(request):
    if request.method == 'POST':
        if request.POST.get('search'):
            # print('ssssssssssssssss')
            found ="T"
            search= request.POST.get('search')
            products1=[]
            categories=Category.objects.all()
            for product in Product.objects.all():
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
                pr1.rate=product.rate
                pr1.email=product.email
                products_S.append(pr1)
            products1=Product.objects.all()
            products=[]
            for product in products1:
                pr1=pr()
                pr1.category=str(product.category)
                pr1.name=product.name
                pr1.description=product.description
                pr1.rate=product.rate
                pr1.email=product.email
                products.append(pr1)
            categories=Category.objects.all()
            print(signed)
            return render(request, 'searchResult.html',{'dash_products':products,'products':products_S,'categories':categories,'found':found,'signed':signed})
def home(request):
    products1=Product.objects.all()
    products=[]
    for product in products1:
        pr1=pr()
        pr1.category=str(product.category)
        pr1.name=product.name
        pr1.description=product.description
        pr1.rate=product.rate
        pr1.email=product.email
        products.append(pr1)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories,'signed':signed})


# def add_fav(request,user_name,product_name):
def register(request):
    f=False
    if request.method == 'POST':
        products1=Product.objects.all()
        products=[]
        for product in products1:
            pr1=pr()
            pr1.category=str(product.category)
            pr1.name=product.name
            pr1.description=product.description
            pr1.rate=product.rate
            pr1.email=product.email
            products.append(pr1)
        categories=Category.objects.all()
        if request.POST.get('type')=='register':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            confirmpassword=request.POST.get('confirmpassword')
            
            data=User(username=username,email=email,password=password)
            print(username)
            print(email)
            print(password)
            print(confirmpassword)
            for user in User.objects.all():
                if user.email==email :
                    f=True
                    break
            if f:
                return render(request, 'registration.html',{'exist':f}) 
            if password != confirmpassword:
                return render(request, 'registration.html',{'exist':f}) 
            data.save()
            signed="T"
            return render(request, 'index.html',{'products':products,'categories':categories,'signed':signed})    
        else :
            email=request.POST.get('email')
            password=request.POST.get('password')
            f=False
            for user in User.objects.all():
                if user.email==email and user.password==password:
                    f=True
                    break
            
            if f==True:
                signed="T"
                return render(request, 'index.html',{'products':products,'categories':categories,'signed':signed})   
            else :
                return render(request, 'registration.html',{'exist':f}) 
             
    return render(request, 'registration.html',{'exist':f}) 
def category_home_page(request,id_):
    products=[]
    for product in Product.objects.all():
        if str(product.category).lower()==id_.lower(): 
            products.append(product)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})
    