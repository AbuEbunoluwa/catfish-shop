from flask import Flask, render_template_string

app = Flask(__name__)

# Mock database of catfish inventory
inventory = [
    {"id": 1, "type": "Fingerlings",       "price": 0.50,  "unit": "per fish", "stock": "In Stock"},
    {"id": 2, "type": "Juveniles",          "price": 1.20,  "unit": "per fish", "stock": "In Stock"},
    {"id": 3, "type": "Table Size (1kg)",   "price": 4.50,  "unit": "per kg",   "stock": "Limited"},
    {"id": 4, "type": "Medium",             "price": 15.00, "unit": "per fish",  "stock": "Available"},
    {"id": 5, "type": "Freshly Smoked",     "price": 3.00,  "unit": "per fish",  "stock": "Available"},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Masterpiece Farm Produce</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f8ff; color: #333; text-align: center; }
        .container { width: 80%; margin: auto; padding: 20px; }
        .product-card {
            background: white; border-radius: 10px; padding: 15px; margin: 10px;
            display: inline-block; width: 220px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-top: 5px solid #1e90ff;
        }
        .price { color: #2e8b57; font-weight: bold; font-size: 1.4em; margin: 10px 0; }
        .btn {
            background: #1e90ff; color: white; border: none;
            padding: 10px 15px; border-radius: 5px; cursor: pointer;
            transition: background 0.3s;
        }
        .btn:hover { background: #0056b3; }
        h1 { color: #000080; margin-bottom: 5px; }
        p.subtitle { color: #555; margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐟 Masterpiece Farm Produce Portal</h1>
        <p class="subtitle">Fresh from the pond to your table.</p>
        <hr>
        {% for item in inventory %}
        <div class="product-card">
            <h3>{{ item.type }}</h3>
            <p class="price">${{ "%.2f"|format(item.price) }}</p>
            <p>{{ item.unit }}</p>
            <p><small style="color: #888;">{{ item.stock }}</small></p>
            <button class="btn" onclick="alert('Order request for {{ item.type }} sent!')">Place Order</button>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
@app.route("/inventory")
def get_inventory():
    return render_template_string(HTML_TEMPLATE, inventory=inventory)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
