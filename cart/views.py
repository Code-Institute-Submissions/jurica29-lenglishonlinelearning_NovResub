from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View, DetailView, ListView
from .models import Item, Order, OrderItem, BillingAddress, Payment, Coupon
from .forms import BillingAddressForm, CouponForm
import stripe
import random
import string
import os

stripe.api_key = settings.STRIPE_SECRET_KEY

if os.path.exists("env.py"):
  import env 

def create_order_code():
    """Creating unique code for orders"""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

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
            return redirect("cart:summary")
        else:
            messages.info(request, "Item added to your cart")
            order.items.add(order_item)
            return redirect("baseapp:home")
    
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("cart:summary")

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
            return redirect("cart:summary")
        else:
            messages.info(request, "Item was not in your cart")
            return redirect("baseapp:home", slug=slug)
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
                'order': order,
                'couponform': CouponForm(),
                'display_coupon_form': True
            }
            return render(self.request, 'billing-address.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, 'You do not have an active order.')
            return redirect('cart:summary')
    
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
                return redirect('cart:payment')

        except ObjectDoesNotExist:
            messages.info(self.request, "No active order found.")
            return redirect('cart:summary')

def get_coupon(request, code):
    """Get coupon function"""
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon is not valid")
        return redirect('cart:billing-address')


class addCouponView(View):
    """Add coupon functionality"""
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Coupon added")
                return redirect('cart:billing-address')
            except ObjectDoesNotExist:
                messages.success(self.request, "You do not have an active order")
                return redirect('baseapp:home')

class PaymentView(View):
    """Class for payment view"""
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
                'display_coupon_form': False,
                'stripe_public_key': stripe.api_key
            }
            return render(self.request, 'payment.html', context)
        else:
            messages.warning(self.request, 'Please add your billing address.')
            return redirect('cart:billing-address')
    
    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.total_price() * 100)
        stripe.api_key = stripe.api_key
        
        try:
            charge = stripe.Charge.create(
                amount = amount,
                currency = 'eur',
                source = token,
                description = 'Payment from Lenglishonlinelearning'
            )

            payment = Payment()
            payment.stripe_charge_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.total_price()
            payment.save()

            order_items = order.items.all()
            order_items.update(ordered=True)

            for item in order_items:
                item.save()

            order.ordered = True
            order.payment = payment

            order.order_ref = create_order_code()
            order.save()

            messages.success(
                self.request,
                "Your order was successful! You will receive a\
                    confirmation email.")
            return redirect(f'/order_success/{order.pk}')
            # return redirect(reverse("order_success", kwargs={"pk": order.pk }))


        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("/")
        except stripe.error.RateLimitError as e:
            messages.warning(self.reqiest, "Rate Limit Error")
        except stripe.error.InvalidRequestError as e:
            messages.warning(self.reqiest, "Invalid paremeters")
            print("Invalid parameters", e)
            print("the value is: ", amount)
            return redirect("/")
        except stripe.error.AuthenticationError as e:
            messages.warning(self.request, "Not authenticated")
            return redirect("/")
        except stripe.error.APIConnectionError as e:
            messages.warning(self.request, "Network Error")
            return redirect("/")
        except stripe.error.StripeError as e:
            messages.warning(self.request, "Something went wrong, you were not charged, please try again.")
        except Exception as e:
            messages.warning(self.request, "Something went wrong, we will work on it since we have been notified.")
            return redirect("/")

def MyOrders(request):
    orders = Order.objects.filter(user=request.user, ordered=True).order_by('-id')
    return render(request, 'order-history.html', {'orders': orders})

@login_required
def order_success(request, pk):
    """
    Show an order confirmation page once purchase is completed
    """
    order = Order.objects.get(pk=pk)

    if order.user == request.user:
        template = render_to_string('email_message.html', {'name': request.user})
        email = EmailMessage(
            'Thank you for your purchase! I will be in touch with you soon to schedule lesson/s.',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        email.fail_silently = False
        email.send()

        context = {'order': order}

        return render(request, 'baseapp/home.html', context)
