from django.urls import path 
from . import views

app_name = 'baseapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetailView, name="productdetail"),
    path('about/', views.AboutView.as_view(), name='about'),
]