from django.shortcuts import render

from .models import MainCategory, Category, Product

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from django.urls import reverse

from django.contrib.auth import authenticate, login as user_login, logout as user_logout

def index(request):
    question = "xxx"
    return render(request, 'store/index.html', {'question': question})

def shop(request, category_id):
    categories = Category.objects.all() 
    main_categories = MainCategory.objects.all()
    if(category_id == 0):
        products = Product.objects.all()
    else:
        category = Category.objects.get(pk = category_id)
        products = category.product_set.all
    return render(request, 'store/shop.html', {'products': products, 'categories': categories, 'main_categories': main_categories})

def product(request, product_id):
    product = Product.objects.get(pk = 1)
    return render(request, 'store/product.html', {'product': product})

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

# def login(request):
#     if request.method == 'POST' :
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user :
#             user_login(request, user)
#             return render(request, 'store/user.html')
#         else :
#             return HttpResponse("invalid")
#     return render(request, 'store/login.html')

# def logout(request):
#     user_logout(request)
#     return render(request, 'store/login.html')

# def user(request):
#     return render(request, 'store/user.html')