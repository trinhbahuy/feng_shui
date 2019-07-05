from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from django.urls import reverse

from django.contrib.auth import authenticate, login as user_login, logout as user_logout

def index(request):
    question = "xxx"
    return render(request, 'store/index.html', {'question': question})
def shop(request):
    return render(request, 'store/shop.html')

def product(request):
    return render(request, 'store/product.html')

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