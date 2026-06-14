import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Database helper ---
# We use this function every time we need to talk to the database.
# It returns rows as dictionaries (e.g., row["name"]) instead of plain tuples,
# which makes the code much easier to read.
def get_db_connection():
    connection = sqlite3.connect("catalog.db")
    connection.row_factory = sqlite3.Row  # lets us access columns by name
    return connection


# --- Home page ---
# Shows all products, with optional search and category filter.
@app.route("/")
def home():
    search = request.args.get("search", "").strip()      # ?search=iphone
    category = request.args.get("category", "").strip()  # ?category=Mac

    connection = get_db_connection()

    # Build the query dynamically based on what the user typed
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if search:
        query += " AND (name LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if category:
        query += " AND category = ?"
        params.append(category)

    products = connection.execute(query, params).fetchall()

    # Fetch distinct categories for the filter dropdown
    categories = connection.execute(
        "SELECT DISTINCT category FROM products ORDER BY category"
    ).fetchall()

    connection.close()

    return render_template(
        "home.html",
        products=products,
        categories=categories,
        search=search,
        selected_category=category,
    )


# --- Add Product ---
# GET  /add → show the empty form
# POST /add → read form data, insert into DB, redirect to home
@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        # Read each field from the submitted form
        name        = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        price       = request.form.get("price", 0)
        category    = request.form.get("category", "").strip()
        image_url   = request.form.get("image_url", "").strip()

        # Insert the new product into the database
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO products (name, description, price, category, image_url) VALUES (?, ?, ?, ?, ?)",
            (name, description, price, category, image_url)
        )
        connection.commit()
        connection.close()

        # After saving, send the user back to the home page
        return redirect(url_for("home"))

    # GET request — just show the empty form
    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(debug=True)