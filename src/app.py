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
    search   = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    sort     = request.args.get("sort", "asc")

    connection = get_db_connection()

    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if search:
        query += " AND (name LIKE ? OR description LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    if category:
        query += " AND category = ?"
        params.append(category)

    if sort == "asc":
        query += " ORDER BY price ASC"
    elif sort == "desc":
        query += " ORDER BY price DESC"

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
        sort=sort,
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


# --- Edit Product ---
# GET  /edit/<id> → find the product, show form pre-filled with its data
# POST /edit/<id> → save the updated data to the database
@app.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    connection = get_db_connection()

    # Fetch the product we want to edit
    # fetchone() returns a single row (or None if not found)
    product = connection.execute(
        "SELECT * FROM products WHERE id = ?", (product_id,)
    ).fetchone()

    if product is None:
        connection.close()
        return "Продукт не найден", 404

    if request.method == "POST":
        # Read the updated values from the form
        name        = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        price       = request.form.get("price", 0)
        category    = request.form.get("category", "").strip()
        image_url   = request.form.get("image_url", "").strip()

        # Update the existing row in the database
        connection.execute(
            """UPDATE products
               SET name = ?, description = ?, price = ?, category = ?, image_url = ?
               WHERE id = ?""",
            (name, description, price, category, image_url, product_id)
        )
        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    # GET request — show the form with current product data
    connection.close()
    return render_template("edit_product.html", product=product)


# --- Product Details ---
@app.route("/product/<int:product_id>")
def product_details(product_id):
    connection = get_db_connection()
    product = connection.execute(
        "SELECT * FROM products WHERE id = ?", (product_id,)
    ).fetchone()
    connection.close()

    if product is None:
        return "Продукт не найден", 404

    return render_template("product_details.html", product=product)


# --- Delete Product ---
# POST /delete/<id> → delete the product from DB → redirect to home
@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("home"))

@app.route("/test")
def test():
    return "Flask works!"


if __name__ == "__main__":
    app.run(debug=True)