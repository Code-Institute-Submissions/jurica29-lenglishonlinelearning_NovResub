from django.urls import path 
from . import views

app_name = 'baseapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='detail'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-item/<slug>/', views.remove_single_item, name='remove-item'),
    path('summary', views.OrderSummaryView.as_view(), name='summary'),
    path('billing-address', views.BillingAddressView.as_view(), name='billing-address'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact')
]