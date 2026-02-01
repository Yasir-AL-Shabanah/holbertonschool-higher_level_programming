import csv
import json
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)


def load_products_from_json(path="products.json"):
    file_path = Path(path)
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    if isinstance(data, list):
        return data
    return []


def load_products_from_csv(path="products.csv"):
    file_path = Path(path)
    if not file_path.exists():
        return []

    products = []
    try:
        with file_path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    except OSError:
        return []

    return products


@app.route("/products")
def products_view():
    """Display products read from JSON or CSV."""
    source = request.args.get("source", type=str)
    product_id = request.args.get("id", type=int)

    error = None
    products = []

    if source == "json":
        products = load_products_from_json()
    elif source == "csv":
        products = load_products_from_csv()
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        filtered = []
        for product in products:
            try:
                pid = int(product.get("id"))
            except (TypeError, ValueError):
                continue
            if pid == product_id:
                filtered.append(product)
        if not filtered:
            error = "Product not found"
            products = []
        else:
            products = filtered

    return render_template("product_display.html", products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
