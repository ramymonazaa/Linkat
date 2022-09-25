from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from .models import Category,Product,User
# Create your views here.
class pr:
    name=""
    email=""
    description=""
    rate=0
    category=""
def home(request):
    if request.method == 'POST':
             if request.POST.get('search'):
                # print('ssssssssssssssss')
                found="T"
                search= request.POST.get('search')
                products1=[]
                categories=Category.objects.all()
                for product in Product.objects.all():
                    if str(product.category).lower()==search.lower() or str(product.name).lower()==search.lower(): 
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
                return render(request, 'searchResult.html',{'dash_products':products,'products':products_S,'categories':categories,'found':found})
    
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
    return render(request, 'index.html',{'products':products,'categories':categories})

def category_home_page(request,id_):
    products=[]
    for product in Product.objects.all():
        if str(product.category).lower()==id_.lower(): 
            products.append(product)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})
    