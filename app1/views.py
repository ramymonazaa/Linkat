from django.shortcuts import render,HttpResponse,redirect
from .models import Category,Product
from .models import User as us
from django.contrib.auth.models import User
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
def profile(request):
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
    user=us.objects.get(username=request.user)
    index=1
    for user1 in us.objects.all():
        print(user1.points)
        if user1==user:
            break;
        index=index+1
    print(index)
    return render(request, 'profile.html',{'user':user,'index':index,'products':products,'categories':categories,'signed':signed})

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
        if str(product.category).lower()==id_.lower(): 
            products.append(product)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})
    