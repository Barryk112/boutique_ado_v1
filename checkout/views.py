from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from bag.context import bag_contents
from django.conf import settings

import stripe

from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currancy=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNJoRFhDA7G5NVkUytYwq2LOrYNTOmlZbQNWVJEy6AwjuCc7PANCbgPRhrJiiCavL9ZxieXqFbvZAPsPG08mi1M00QaFl7tcy',
        'client_secret': 'Test client secret',
    }

    return render(request, template, context)