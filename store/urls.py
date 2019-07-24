from django.urls import path

from . import views

from django.contrib.auth import views as auth_views
app_name = 'store'

urlpatterns = [
    path('', views.index),
    path('shop/<int:category_id>', views.shop),
    path('product/<int:product_id>', views.product),
    path('cart', views.cart),
    path('checkout', views.checkout),
    # path('login', views.login),
    # path('logout', views.logout),
    # path('user', views.user),
    ###########
    # path('login', auth_views.LoginView.as_view())
    # path('<int:product_id>/results', views.results),
]