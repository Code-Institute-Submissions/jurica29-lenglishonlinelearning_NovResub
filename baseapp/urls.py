from django.urls import path 
from . import views

app_name = 'baseapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('about/', views.AboutView.as_view(), name='about')
]
