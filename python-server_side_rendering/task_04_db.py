import csv
import json
import sqlite3
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


def load_products_from_db(path="products.db", product_id=None):
    file_path = Path(path)
    if not file_path.exists():
        return []

    products = []
    connection = None
    try:
        connection = sqlite3.connect(file_path)
        cursor = connection.cursor()
        if product_id is not None:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,),
            )
            rows = cursor.fetchall()
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
        for row in rows:
            products.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": row[3],
                }
            )
    except sqlite3.Error:
        return []
    finally:
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass

    return products


@app.route("/products")
def products_view():
    """Display products from JSON, CSV or SQLite database."""
    source = request.args.get("source", type=str)
    product_id = request.args.get("id", type=int)

    error = None
    products = []

    if source == "json":
        products = load_products_from_json()
    elif source == "csv":
        products = load_products_from_csv()
    elif source == "sql":
        products = load_products_from_db(product_id=product_id)
    else:
        error = "Wrong source"

    if source in ("json", "csv") and not error and product_id is not None:
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
    elif source == "sql" and product_id is not None and not products:
        error = "Product not found"

    return render_template("product_display.html", products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
