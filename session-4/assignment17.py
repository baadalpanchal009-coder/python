# SESSION 4 - Payment Gateway Integration
# Topics: Paytm, Stripe, PayPal Integration, Payment Initiation,
# Transaction Callback, Book Appointment, Pay Now Flow
# ------------------------------------------------------------------------------------


# Task 1: Create a Flask App with an IPL Ticket Payment Form
# File: app.py

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-only-change-me')


@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        amount = request.form.get('amount', type=float)

        if not name or not email or amount is None or amount <= 0:
            return 'Please enter valid payment details.', 400

        return render_template(
            'payment_details.html',
            name=name,
            email=email,
            amount=amount
        )

    return render_template('pay.html')


# File: templates/pay.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>IPL Ticket Booking</title>
</head>
<body>
    <h1>Book IPL Match Tickets</h1>

    <form method="post">
        <label>Name:</label>
        <input type="text" name="name" required>

        <label>Email:</label>
        <input type="email" name="email" required>

        <label>Ticket Amount (INR):</label>
        <input type="number" name="amount" min="1" step="0.01" required>

        <button type="submit">Continue to Payment</button>
    </form>
</body>
</html>
"""

# File: templates/payment_details.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Payment Details</title>
</head>
<body>
    <h1>IPL Ticket Order</h1>
    <p>Name: {{ name }}</p>
    <p>Email: {{ email }}</p>
    <p>Amount: ₹{{ amount }}</p>
    <p>Payment gateway integration comes next.</p>
    <a href="{{ url_for('pay') }}">Back</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 2: Integrate Paytm Sandbox Payment
# Install:
# pip install flask requests paytmchecksum

# Set environment variables before running:
# PAYTM_MID=YOUR_TEST_MID
# PAYTM_MERCHANT_KEY=YOUR_TEST_MERCHANT_KEY
# PAYTM_WEBSITE=WEBSTAGING
# PAYTM_CALLBACK_URL=http://localhost:5000/payment-callback
#
# Use credentials supplied by Paytm's official developer dashboard.
# Never use production credentials for sandbox testing.

# Add to app.py:

import uuid
import requests
from flask import session, abort
from paytmchecksum import PaytmChecksum

PAYTM_HOST = 'https://securegw-stage.paytm.in'


@app.route('/pay-paytm', methods=['POST'])
def pay_paytm():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    amount = request.form.get('amount', type=float)

    if not name or not email or amount is None or amount <= 0:
        return 'Invalid payment details.', 400

    mid = os.environ.get('PAYTM_MID')
    merchant_key = os.environ.get('PAYTM_MERCHANT_KEY')
    callback_url = os.environ.get('PAYTM_CALLBACK_URL')

    if not all([mid, merchant_key, callback_url]):
        return 'Paytm sandbox credentials are not configured.', 500

    order_id = uuid.uuid4().hex

    # Store the expected order amount server-side.
    session['paytm_order'] = {
        'order_id': order_id,
        'amount': f'{amount:.2f}',
        'name': name,
        'email': email
    }

    body = {
        'requestType': 'Payment',
        'mid': mid,
        'websiteName': os.environ.get('PAYTM_WEBSITE', 'WEBSTAGING'),
        'orderId': order_id,
        'callbackUrl': callback_url,
        'txnAmount': {
            'value': f'{amount:.2f}',
            'currency': 'INR'
        },
        'userInfo': {
            'custId': email
        }
    }

    checksum = PaytmChecksum.generateSignature(body, merchant_key)

    payload = {
        'body': body,
        'head': {'signature': checksum}
    }

    try:
        response = requests.post(
            f'{PAYTM_HOST}/theia/api/v1/initiateTransaction',
            params={'mid': mid, 'orderId': order_id},
            json=payload,
            timeout=20
        )
        response.raise_for_status()
        result = response.json()

        txn_token = result.get('body', {}).get('txnToken')

        if not txn_token:
            return 'Unable to initiate Paytm payment.', 502

        return render_template(
            'paytm_redirect.html',
            mid=mid,
            order_id=order_id,
            txn_token=txn_token,
            amount=f'{amount:.2f}'
        )

    except requests.RequestException:
        return 'Paytm sandbox is temporarily unavailable.', 502


# File: templates/paytm_redirect.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Pay with Paytm Sandbox</title>
</head>
<body>
    <h1>Continue to Paytm Sandbox</h1>

    <form method="post"
          action="https://securegw-stage.paytm.in/theia/processTransaction">
        <input type="hidden" name="mid" value="{{ mid }}">
        <input type="hidden" name="orderId" value="{{ order_id }}">
        <input type="hidden" name="txnToken" value="{{ txn_token }}">

        <p>Amount: ₹{{ amount }}</p>
        <button type="submit">Proceed to Paytm</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 3: Handle Paytm Payment Callback and Verify Status

# Add to app.py:

from flask import jsonify


@app.route('/payment-callback', methods=['POST', 'GET'])
def payment_callback():
    merchant_key = os.environ.get('PAYTM_MERCHANT_KEY')
    mid = os.environ.get('PAYTM_MID')

    if not merchant_key or not mid:
        return 'Payment configuration error.', 500

    callback_data = request.form.to_dict()

    if not callback_data:
        callback_data = request.args.to_dict()

    received_checksum = callback_data.pop('CHECKSUMHASH', None)

    if not received_checksum:
        return 'Missing payment signature.', 400

    if not PaytmChecksum.verifySignature(
        callback_data,
        merchant_key,
        received_checksum
    ):
        return 'Invalid payment signature.', 400

    expected_order = session.get('paytm_order', {})
    order_id = callback_data.get('ORDERID')

    if not expected_order or order_id != expected_order.get('order_id'):
        return 'Order does not match the current session.', 400

    # Do not trust callback status alone. Verify the transaction
    # against Paytm's official transaction-status API before fulfillment.
    status_body = {
        'mid': mid,
        'orderId': order_id
    }

    status_signature = PaytmChecksum.generateSignature(
        status_body,
        merchant_key
    )

    try:
        response = requests.post(
            f'{PAYTM_HOST}/v3/order/status',
            json={
                'body': status_body,
                'head': {'signature': status_signature}
            },
            timeout=20
        )
        response.raise_for_status()
        status_result = response.json().get('body', {})

    except requests.RequestException:
        return 'Unable to verify payment status. Try again later.', 502

    expected_amount = expected_order.get('amount')
    paid_amount = status_result.get('txnAmount')
    txn_status = status_result.get('resultInfo', {}).get('resultStatus')

    success = (
        status_result.get('orderId') == order_id
        and txn_status == 'TXN_SUCCESS'
        and paid_amount is not None
        and f'{float(paid_amount):.2f}' == expected_amount
    )

    return render_template(
        'payment_result.html',
        success=success,
        order_id=order_id
    )


# File: templates/payment_result.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Payment Result</title>
</head>
<body>
    {% if success %}
        <h1>Payment Successful!</h1>
        <p>Your order has been paid successfully.</p>
    {% else %}
        <h1>Payment Failed or Pending</h1>
        <p>Please verify your transaction before trying again.</p>
    {% endif %}

    <p>Order ID: {{ order_id }}</p>
    <a href="/pay">Return to Booking</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 4: Integrate Stripe Test Payment for a Food Order
# Install:
# pip install stripe

# Set environment variables:
# STRIPE_SECRET_KEY=sk_test_YOUR_TEST_SECRET_KEY
# STRIPE_PUBLISHABLE_KEY=pk_test_YOUR_TEST_PUBLISHABLE_KEY
# STRIPE_SUCCESS_URL=http://localhost:5000/stripe-success
# STRIPE_CANCEL_URL=http://localhost:5000/stripe-cancel

import stripe

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


@app.route('/food-order', methods=['GET', 'POST'])
def food_order():
    if request.method == 'POST':
        dish = request.form.get('dish', '').strip()
        price = request.form.get('price', type=float)

        if not dish or price is None or price <= 0:
            return 'Invalid food order.', 400

        # In a real application, retrieve the price from the database.
        # Never trust a client-supplied price for a real payment.
        amount_in_paise = round(price * 100)

        checkout = stripe.checkout.Session.create(
            mode='payment',
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {'name': dish},
                    'unit_amount': amount_in_paise,
                },
                'quantity': 1,
            }],
            success_url=(
                os.environ.get('STRIPE_SUCCESS_URL')
                + '?session_id={CHECKOUT_SESSION_ID}'
            ),
            cancel_url=os.environ.get('STRIPE_CANCEL_URL'),
        )

        return redirect(checkout.url, code=303)

    return render_template('food_order.html')


@app.route('/stripe-success')
def stripe_success():
    session_id = request.args.get('session_id')

    if not session_id:
        return 'Missing checkout session.', 400

    try:
        checkout = stripe.checkout.Session.retrieve(session_id)

        if checkout.payment_status == 'paid':
            return render_template(
                'stripe_result.html',
                message='Food order payment successful!'
            )

        return render_template(
            'stripe_result.html',
            message='Payment is not completed yet.'
        )

    except stripe.StripeError:
        return 'Unable to verify Stripe payment.', 502


@app.route('/stripe-cancel')
def stripe_cancel():
    return render_template(
        'stripe_result.html',
        message='Payment was cancelled.'
    )


# File: templates/food_order.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Food Order Payment</title>
</head>
<body>
    <h1>Order Food</h1>

    <form method="post">
        <label>Dish Name:</label>
        <input type="text" name="dish" required>

        <label>Price (INR):</label>
        <input type="number" name="price" min="1" step="0.01" required>

        <button type="submit">Pay Now</button>
    </form>
</body>
</html>
"""

# File: templates/stripe_result.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Payment Result</title>
</head>
<body>
    <h1>{{ message }}</h1>
    <a href="/food-order">Back to Food Orders</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 5: PayPal Sandbox Integration for IPL Tickets
# Install:
# pip install paypalrestsdk

# Configure PayPal sandbox credentials as environment variables:
# PAYPAL_CLIENT_ID=YOUR_SANDBOX_CLIENT_ID
# PAYPAL_CLIENT_SECRET=YOUR_SANDBOX_CLIENT_SECRET

# Note: paypalrestsdk is a legacy SDK. For a new project, use
# PayPal's current Checkout Server SDK or REST API documentation.
# The following example illustrates the older SDK workflow.

import paypalrestsdk


def configure_paypal():
    paypalrestsdk.configure({
        'mode': 'sandbox',
        'client_id': os.environ.get('PAYPAL_CLIENT_ID'),
        'client_secret': os.environ.get('PAYPAL_CLIENT_SECRET')
    })


@app.route('/paypal-pay', methods=['POST'])
def paypal_pay():
    configure_paypal()

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    amount = request.form.get('amount', type=float)

    if not name or not email or amount is None or amount <= 0:
        return 'Invalid ticket details.', 400

    payment = paypalrestsdk.Payment({
        'intent': 'sale',
        'payer': {'payment_method': 'paypal'},
        'redirect_urls': {
            'return_url': url_for('paypal_success', _external=True),
            'cancel_url': url_for('paypal_cancel', _external=True)
        },
        'transactions': [{
            'item_list': {
                'items': [{
                    'name': 'IPL Match Ticket',
                    'sku': 'IPL-TICKET',
                    'price': f'{amount:.2f}',
                    'currency': 'USD',
                    'quantity': 1
                }]
            },
            'amount': {
                'total': f'{amount:.2f}',
                'currency': 'USD'
            },
            'description': f'IPL ticket for {name}'
        }]
    })

    if payment.create():
        session['paypal_payment_id'] = payment.id
        session['paypal_payer_email'] = email

        for link in payment.links:
            if link.rel == 'approval_url':
                return redirect(link.href)

        return 'PayPal approval URL was not returned.', 502

    return 'Unable to create PayPal payment.', 502


@app.route('/paypal-success')
def paypal_success():
    configure_paypal()

    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    if (
        not payment_id
        or not payer_id
        or payment_id != session.get('paypal_payment_id')
    ):
        return 'Invalid payment callback.', 400

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({'payer_id': payer_id}):
        session.pop('paypal_payment_id', None)

        return render_template(
            'payment_result.html',
            success=True,
            order_id=payment_id
        )

    return render_template(
        'payment_result.html',
        success=False,
        order_id=payment_id
    )


@app.route('/paypal-cancel')
def paypal_cancel():
    return 'PayPal payment was cancelled.'


# ------------------------------------------------------------------------------------


# Main Application URLs:
#
# http://127.0.0.1:5000/pay
# http://127.0.0.1:5000/pay-paytm
# http://127.0.0.1:5000/food-order
# http://127.0.0.1:5000/paypal-pay
#
# Run the application:
# python app.py
#
# Add this at the bottom of app.py:

if __name__ == '__main__':
    app.run(debug=True)


# ------------------------------------------------------------------------------------


# Important Concepts
#
# Payment initiation:
# Creates a transaction with the payment gateway.
#
# Payment callback:
# Receives the result after the payment process.
#
# Signature verification:
# Checks that the callback has not been tampered with.
#
# Server-side status verification:
# Confirms payment directly with the payment gateway.
#
# Sandbox:
# A test environment for mock payments.
#
# Security:
# Never trust a payment success URL alone.
# Verify the transaction status and amount on the server.
# Keep API secrets in environment variables.
# Use HTTPS, CSRF protection and database-backed order records
# before deploying a real payment application.
#
# ------------------------------------------------------------------------------------