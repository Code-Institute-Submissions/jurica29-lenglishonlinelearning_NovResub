from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, ListView
from cart.models import Item

class HomeView(ListView):
    """Home page view"""
    model = Item
    paginate_by = 8
    template_name = 'home.html'

class AboutView(ListView):
    """About page view"""
    model = Item
    template_name = 'about.html'

class ProductDetailView(DetailView):
    """Product detail view"""
    model = Item
    template_name = 'productdetail.html'
