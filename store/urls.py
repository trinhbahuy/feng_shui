from django.urls import path

from . import views

from django.contrib.auth import views as auth_views
app_name = 'store'

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('product', views.product)
    # path('login', views.login),
    # path('logout', views.logout),
    # path('user', views.user),
    ###########
    # path('login', auth_views.LoginView.as_view())
    # path('<int:product_id>/results', views.results),
]