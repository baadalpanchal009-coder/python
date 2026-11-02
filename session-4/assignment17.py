
from flask import Flask, render_template_string, request, redirect, url_for
import stripe
import paypalrestsdk

app = Flask(__name__)
app.secret_key = "my_secret_key"

# ---------------- HOME / PAYMENT FORM ----------------

@app.route('/pay')
def pay():
    return render_template_string("""
    <h2>IPL Match Ticket Booking</h2>
    <form action="/paytm" method="POST">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Amount: <input type="number" name="amount" required><br><br>
        <button type="submit">Pay Now</button>
    </form>
    """)


# ---------------- PAYTM PAYMENT ----------------

@app.route('/paytm', methods=['POST'])
def paytm():
    name = request.form['name']
    email = request.form['email']
    amount = request.form['amount']

    # Paytm sandbox integration placeholder.
    # Add Paytm test merchant credentials and initiate
    # transaction using the official Paytm SDK/API.

    return render_template_string("""
    <h2>IPL Ticket Payment</h2>
    <p>Name: {{name}}</p>
    <p>Email: {{email}}</p>
    <p>Amount: ₹{{amount}}</p>
    <p>Paytm Sandbox Payment Initiated</p>
    <a href="/payment-callback?status=success">
        Simulate Successful Payment
    </a><br><br>
    <a href="/payment-callback?status=failed">
        Simulate Failed Payment
    </a>
    """, name=name, email=email, amount=amount)


@app.route('/payment-callback')
def payment_callback():
    status = request.args.get('status')

    if status == 'success':
        return "<h2>Payment Successful!</h2>"
    else:
        return "<h2>Payment Failed!</h2>"


# ---------------- STRIPE PAYMENT ----------------

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"


@app.route('/food-order', methods=['GET', 'POST'])
def food_order():
    if request.method == 'POST':
        dish = request.form['dish']
        price = float(request.form['price'])

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': dish,
                        },
                        'unit_amount': int(price * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=url_for(
                    'success', _external=True
                ),
                cancel_url=url_for(
                    'failure', _external=True
                ),
            )

            return redirect(session.url)

        except Exception as e:
            return str(e)

    return render_template_string("""
    <h2>Zomato Food Order</h2>
    <form method="POST">
        Dish Name:
        <input type="text" name="dish" required><br><br>
        Price:
        <input type="number" name="price" required><br><br>
        <button type="submit">Pay Now</button>
    </form>
    """)


@app.route('/success')
def success():
    return "<h2>Stripe Payment Successful!</h2>"


@app.route('/failure')
def failure():
    return "<h2>Payment Cancelled or Failed!</h2>"


# ---------------- PAYPAL PAYMENT ----------------

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})


@app.route('/paypal', methods=['GET', 'POST'])
def paypal():
    if request.method == 'POST':

        amount = request.form['amount']

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://localhost:5000/paypal-success",
                "cancel_url": "http://localhost:5000/paypal-cancel"
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": "IPL Match Ticket Booking"
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)

        return "PayPal Payment Creation Failed"

    return render_template_string("""
    <h2>PayPal IPL Ticket Payment</h2>
    <form method="POST">
        Enter Ticket Amount (USD):
        <input type="number" name="amount"
               step="0.01" required>
        <button type="submit">Pay with PayPal</button>
    </form>
    """)


@app.route('/paypal-success')
def paypal_success():
    return "<h2>PayPal Payment Successful (Demo)</h2>"


@app.route('/paypal-cancel')
def paypal_cancel():
    return "<h2>PayPal Payment Cancelled</h2>"


# ---------------- RUN FLASK APP ----------------

if __name__ == '__main__':
    app.run(debug=True)
