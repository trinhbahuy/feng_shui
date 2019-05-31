from django.urls import path

from . import views

# app_name = 'polls'

urlpatterns = [
    path('', views.index),
    # path('<int:product_id>/', views.detail),
    # path('<int:product_id>/results', views.results),
]