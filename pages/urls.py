from django.urls import path
from .views import homePageView, ProductIndexView, ProductShowView, ProductCreateView  


urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]