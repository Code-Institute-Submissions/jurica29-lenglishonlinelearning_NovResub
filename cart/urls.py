from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path("remove-item/<slug>/", views.remove_single_item, name="remove-item"),
    path("summary", views.OrderSummaryView.as_view(), name="summary"),
    path("billing-address", views.BillingAddressView.as_view(), name="billing-address"),
    path("add-coupon/", views.addCouponView.as_view(), name="add-coupon"),
    path("order-history/", views.MyOrders, name="order-history"),
    path("payment/", views.PaymentView.as_view(), name="payment"),
]
