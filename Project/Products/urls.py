from . import views
from django.urls import path

app_name = 'Products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('get-status/', views.ProductCount.as_view(), name='get_status'),
    path('get-status/<str:pk>', views.ProductDetail.as_view(), name='product_detail'),
]