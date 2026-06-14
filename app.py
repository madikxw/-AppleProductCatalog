from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add")
def add_product():
    return render_template("add_product.html")

@app.route("/edit/<int:product_id>")
def edit_product(product_id):
    return render_template("edit_product.html")

@app.route("/product/<int:product_id>")
def product_details(product_id):
    return render_template("product_details.html")


if __name__ == "__main__":
    app.run(debug=True)
