from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from profiles.models import UserProfile

import stripe


def subscriptions(request):
    """ A view to return the subscriptions page """

    return render(request, 'subscriptions/subscriptions.html')


@login_required
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://8000-c258c6d1-b0ff-4fce-b6f4-eb72b8f7ec16.ws-eu03.gitpod.io/subscriptions/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'subscription_success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'subscription_cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def subscription_success(request):
    return render(request, 'subscriptions/subscription_success.html')


@login_required
def subscription_cancel(request):
    return render(request, 'subscriptions/subscription_cancel.html')