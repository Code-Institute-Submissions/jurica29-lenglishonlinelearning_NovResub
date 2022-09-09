from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, ListView
from .models import Item, Order, OrderItem
# Views for pages

class HomeView(ListView):
    """Home page view"""
    model = Item
    paginate_by = 8
    template_name = 'home.html'

class ProductDetailView(DetailView):
    """Product detail view"""
    model = Item
    template_name = 'productdetail.html'

@login_required(login_url="/accounts/login/")
def add_to_cart(request, slug):
    """Function for ordering functionality"""
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
    )

    order_q = Order.objects.filter(user=request.user, ordered=False)

    if order_q.exists():
        order = order_q[0]
    
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item added to your cart")
            return redirect("baseapp:summary")
        else:
            messages.info(request, "Item added to your cart")
            order.items.add(order_item)
            return redirect("baseapp:summary")
    
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("baseapp:summary")

class OrderSummaryView(LoginRequiredMixin, View):
    """View for order summary page"""
    def get(self, *args, **kwargs):
        try:
            current_order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': current_order
            }
            return render(self.request, 'summary.html', context)

        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order.")
            return redirect('/')

        return render(self.request, 'summary.html', context)