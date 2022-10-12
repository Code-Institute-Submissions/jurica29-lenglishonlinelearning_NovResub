from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, ListView
from cart.models import Item
from .forms import ProductReviewForm


class HomeView(ListView):
    """Home page view"""
    model = Item
    paginate_by = 8
    template_name = 'home.html'


class AboutView(ListView):
    """About page view"""
    model = Item
    template_name = 'about.html'

def ProductDetailView(request, slug):
    """Function view used for detail page functionality/display."""
    item = get_object_or_404(Item, slug=slug)

    if request.method == "POST":
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.name = request.user.username
            review.save()

            return redirect("baseapp:productdetail", slug=slug)
    else:
        form = ProductReviewForm()

    return render(request, "productdetail.html", {"item": item, "form": form})