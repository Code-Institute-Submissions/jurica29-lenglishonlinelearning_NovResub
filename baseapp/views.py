from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, ListView
from .models import Item, Order, OrderItem, BillingAddress
from .forms import BillingAddressForm
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

@login_required(login_url="/accounts/login/")
def remove_single_item(request, slug):
    """Function for removing single item from cart"""
    item = get_object_or_404(Item, slug=slug)

    order_q = Order.objects.filter(user=request.user, ordered=False)

    if order_q.exists():
        order = order_q[0]
    
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)

            messages.info(request, "Cart updated")
            return redirect("baseapp:summary")

        else:
            messages.info(request, "Item was not in your cart")
            return redirect("baseapp:productdetail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("baseapp:productdetail", slug=slug)

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

class BillingAddressView(View):
    """View for billing address"""
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = BillingAddressForm()
            context = {
                'form': form,
                'order': order
            }
            return render(self.request, 'billing-address.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, 'You do not have an active order.')
            return redirect('baseapp:summary')
    
    def post(self, *args, **kwargs):
        """Function that makes billing address form work"""
        form = BillingAddressForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip_code = form.cleaned_data.get('zip_code')

                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment = apartment_address,
                    country = country,
                    zip = zip_code
                )

                billing_address.save()
                order.billing_address = billing_address
                order.save()

                messages.info(self.request, "Billing address added to your order.")
                return redirect('baseapp:payment')

        except ObjectDoesNotExist:
            messages.info(self.request, "No active order found.")
            return redirect('baseapp:summary')

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
            }
            return render(self.request, 'payment.html', context)
        else:
            messages.warning(self.request, 'Please add your billing address.')
            return redirect('baseapp:billing-address')