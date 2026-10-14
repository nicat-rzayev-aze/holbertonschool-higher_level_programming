#!/usr/bin/env python3
import json
import csv
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ---------- TASK 1: Static Pages ----------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# ---------- TASK 2: Dynamic Items ----------

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


# ---------- TASK 3|&4: Products JSON/CSV/DATABASE ----------

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Strip whitespace
                row = {k.strip(): v.strip() for k, v in row.items()}
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def read_sqlite(db_path):
    data = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except sqlite3.Error:
        data = []
    return data

# ---------- Routes ----------

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    error = None
    products_list = []

    if source == 'json':
        products_list = read_json('products.json')
    elif source == 'csv':
        products_list = read_csv('products.csv')
    elif source == 'sql':
        products_list = read_sqlite('products.db')
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        filtered = [p for p in products_list if p['id'] == product_id]
        if filtered:
            products_list = filtered
        else:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)


# ---------- Run server ----------

if __name__ == '__main__':
    app.run(debug=True, port=5000)
