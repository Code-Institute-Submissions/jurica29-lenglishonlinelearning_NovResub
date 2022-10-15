""" System Module """
from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("productdetail/<slug>/", views.ProductDetailView, name="productdetail"),
    path("deletereview/<str:pk>/", views.deleteReview, name="deleteReview"),
    path("editreview/<str:pk>/", views.editReview, name="editReview"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("privacypolicy/", views.PrivacyPolicy.as_view(), name="privacypolicy"),
]
