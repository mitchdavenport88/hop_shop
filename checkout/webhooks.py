from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks """

    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Webhook handler class
    handler = StripeWH_Handler(request)

    # Webhook events we're listening for / relevant handler functions
    event_map = {
        'payment_intent.succeeded': (
            handler.handle_payment_intent_succeeded),
        'payment_intent.payment_failed': (
            handler.handle_payment_intent_payment_failed),
    }

    # Get webhook type from Stripe
    event_type = event['type']

    # If there's a match in the event map dictionary we get it
    # We use the generic handle_event otherwise
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
