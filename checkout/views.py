from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNJoRFhDA7G5NVkUytYwq2LOrYNTOmlZbQNWVJEy6AwjuCc7PANCbgPRhrJiiCavL9ZxieXqFbvZAPsPG08mi1M00QaFl7tcy',
        'client_secret': 'Test client secret',
    }

    return render(request, template, context)