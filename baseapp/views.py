""" System Module """
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from cart.models import Item
from .models import ProductReview
from .forms import ProductReviewForm


class HomeView(ListView):
    """Home page view"""

    model = Item
    paginate_by = 8
    template_name = "home.html"


class AboutView(ListView):
    """About page view"""

    model = Item
    template_name = "about.html"


class PrivacyPolicy(TemplateView):
    """Privacy policy page view"""

    template_name = "privacypolicy.html"


def ProductDetailView(request, slug):
    """Function view used for detail page functionality/display."""
    item = get_object_or_404(Item, slug=slug)

    # Get the reviews posted by the user for the item
    user_reviews = item.reviews.filter(name=request.user.username)

    if request.method == "POST":
        form = ProductReviewForm(request.POST)

        # Check if there are any reviews posted by the user
        if user_reviews:
            # If there are any, raise an error
            messages.error(request, "You have already left a review!")
            raise PermissionDenied

        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.name = request.user.username
            review.save()

            messages.success(request, "Thank you for leaving a review!")
            return redirect("baseapp:productdetail", slug=slug)
    else:
        form = ProductReviewForm()

    return render(request, "productdetail.html", {"item": item, "form": form})


def deleteReview(request, pk):
    """Function view used for deleting review."""
    review = ProductReview.objects.get(id=pk)

    if request.method == "POST":
        review.delete()

        messages.success(request, "Review deleted!")
        return redirect("baseapp:productdetail", review.item.slug)

    context = {"item": review}

    return render(request, "deletereview.html", context)


def editReview(request, pk):
    """Function view used for editing review."""
    review = ProductReview.objects.get(id=pk)
    form = ProductReviewForm(instance=review)

    if request.method == "POST":
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()

        messages.success(request, "Review edited!")
        return redirect("baseapp:productdetail", review.item.slug)

    context = {"form": form, "review": review}

    return render(request, "editreview.html", context)
