import stripe
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from .models import Item
from django.shortcuts import get_object_or_404, render, redirect


stripe.api_key = settings.STRIPE_SECRET_KEY


def item(request: HttpRequest, pk: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)
    context = {"item": item, "STRIPE_SECRET_KEY" : settings.STRIPE_SECRET_KEY}
    return render(request, "item/item.html", context)


def buy(request: HttpRequest, pk: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=pk)
    domain = "http://127.0.0.1:8000"
    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'rub',
            'product_data': {
            'name': item.name,
            },
            'unit_amount': item.price,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url=domain + '/success/',
        cancel_url=domain + '/cancel/',
    )
    return redirect(session.url)


def success(request: HttpRequest) -> HttpResponse:
    return render(request, "item/success.html")


def cancel(request: HttpRequest) -> HttpResponse:
    return render(request, "item/cancel.html")