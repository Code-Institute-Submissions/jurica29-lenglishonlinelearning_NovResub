from django.urls import path 
from . import views
from .webhooks import webhook

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-item/<slug>/', views.remove_single_item, name='remove-item'),
    path('summary', views.OrderSummaryView.as_view(), name='summary'),
    path('billing-address', views.BillingAddressView.as_view(), name='billing-address'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('wh/', webhook, name='webhook'),
]