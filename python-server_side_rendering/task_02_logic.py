import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


def load_items(path="items.json"):
    """Load list of items from a JSON file."""
    file_path = Path(path)
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    items = data.get("items", [])
    if not isinstance(items, list):
        return []
    return items


@app.route("/items")
def items_view():
    """Render items list page."""
    items = load_items()
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
