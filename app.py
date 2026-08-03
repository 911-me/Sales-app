"""
Simple Sales Recording Web Application
---------------------------------------
Assignment II - Python Programming

This is the backend of the application, built using Flask (a lightweight
Python web framework). It manages sales data using core Python concepts:
variables, data types, lists, dictionaries, and control flow.

The backend:
    1. Stores sales records in a list of dictionaries (in-memory, per session).
    2. Renders an HTML page where the shop owner can enter a sale.
    3. Handles form submissions (POST) to add new sales.
    4. Calculates the total sales amount automatically.
    5. Supports deleting a single record and clearing all records.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------------------------------------------------------------------
# In-memory data store
# ---------------------------------------------------------------------------
# A list of dictionaries is used to hold each sale record.
# Each dictionary has: product (str), quantity (int), price (float), total (float)
sales_records = []


def calculate_total(quantity, price):
    """Return the total sale amount for a given quantity and unit price."""
    return quantity * price


def calculate_day_total(records):
    """Return the sum of all sale totals currently recorded."""
    day_total = 0
    for record in records:
        day_total += record["total"]
    return day_total


@app.route("/", methods=["GET"])
def index():
    """Display the sales entry form and the list of sales entered so far."""
    grand_total = calculate_day_total(sales_records)
    return render_template(
        "index.html",
        sales=sales_records,
        grand_total=grand_total,
        record_count=len(sales_records),
    )


@app.route("/add", methods=["POST"])
def add_sale():
    """Handle the form submission and add a new sale to the record list."""
    product = request.form.get("product", "").strip()
    quantity_raw = request.form.get("quantity", "")
    price_raw = request.form.get("price", "")

    # Basic validation using control flow (if / else)
    try:
        quantity = int(quantity_raw)
        price = float(price_raw)
    except ValueError:
        # If conversion fails, ignore the bad submission and go back.
        return redirect(url_for("index"))

    if product == "" or quantity <= 0 or price <= 0:
        return redirect(url_for("index"))

    total = calculate_total(quantity, price)

    # A dictionary represents one sale record.
    new_sale = {
        "id": len(sales_records) + 1,
        "product": product,
        "quantity": quantity,
        "price": price,
        "total": total,
    }

    sales_records.append(new_sale)
    return redirect(url_for("index"))


@app.route("/delete/<int:sale_id>", methods=["POST"])
def delete_sale(sale_id):
    """Remove a single sale record by its id."""
    global sales_records
    sales_records = [s for s in sales_records if s["id"] != sale_id]
    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear_sales():
    """Clear all sales records (start a new day)."""
    sales_records.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    # debug=True is useful during development; turn off for production/deployment.
    app.run(debug=True)
