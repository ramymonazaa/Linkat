from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from .models import Category,Product,User
# Create your views here.
def home(request):
    if request.method == 'POST':
             if request.POST.get('search'):
                # print('ssssssssssssssss')
                found="T"
                search= request.POST.get('search')
                products=[]
                categories=Category.objects.all()
                for product in Product.objects.all():
                    if str(product.category)==search or str(product.name)==search: 
                        products.append(product)
                if len(products)==0:
                    found="F"
                return render(request, 'searchResult.html',{'products':products,'categories':categories,'found':found})
    
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})

def category_home_page(request,id_):
    products=[]
    for product in Product.objects.all():
        if str(product.category)==id_: 
            products.append(product)
    categories=Category.objects.all()
    return render(request, 'index.html',{'products':products,'categories':categories})
    