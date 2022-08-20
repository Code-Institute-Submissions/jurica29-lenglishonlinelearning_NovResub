from django.shortcuts import render
from .models import Item
from django.views.generic import View, DetailView, ListView
# Create your views here.

class HomeView(ListView):
    model = Item
    paginate_by = 8
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = Item
    template_name = 'productdetail.html'