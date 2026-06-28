🍎 Apple Product Catalog

A Flask-based web application for browsing and managing a catalogue of Apple products with search, filtering, sorting, and full CRUD operations.

Educational Practice Project · Astana IT University · 2026

⸻

👨‍💻 Author

Bissentayev Madiyar

First-Year Student
Astana IT University

⸻

📖 Project Overview

Apple Product Catalog is a full-stack web application developed using Python, Flask, and SQLite. The project demonstrates the implementation of CRUD operations, searching, filtering, sorting, and database management within a modern web application.

The application follows a three-layer architecture:

* 🎨 Presentation Layer — HTML, Bootstrap 5, Jinja2
* ⚙️ Application Layer — Flask
* 💾 Data Layer — SQLite

⸻

✨ Features

* 📱 Browse Apple products
* 🔍 Search by product name and description
* 🗂 Filter products by category
* 💲 Sort products by price
* 📄 View product details
* ➕ Add new products
* ✏️ Edit existing products
* 🗑 Delete products with confirmation
* 💾 SQLite database persistence

⸻

🛠 Technologies

* Python 3
* Flask
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* Jinja2
* pytest
* Git
* GitHub Actions

⸻

🚀 Getting Started

Clone the repository

git clone https://github.com/YOUR_USERNAME/apple-product-catalog.git
cd apple-product-catalog

Install dependencies

pip install -r requirements.txt

Initialize the database

python src/init_db.py

Run the application

python src/app.py

Open your browser:

http://127.0.0.1:5000

⸻

📂 Project Structure

(Insert your project structure image here.)

⸻

🔍 Search & Filtering

The application allows users to:

* Search products by name and description
* Filter products by category
* Sort products by price (ascending or descending)
* Combine all filters in a single request

⸻

💾 Database

Database: SQLite

Table: products

Columns:

* id
* name
* description
* price
* category
* image_url

The database contains 25 sample Apple products.

⸻

🧪 Testing

Run all tests:

pytest tests/

The test suite validates:

* Repository structure
* CRUD functionality
* Application behavior

⸻

⚡ Challenges

During development, several challenges were encountered:

* Learning Flask
* Designing the database
* Connecting backend and frontend
* Implementing SQL search and filtering
* Configuring GitHub Actions
* Testing and debugging the application

⸻

🚀 Future Improvements

* User authentication
* Role-based authorization
* SQLAlchemy ORM
* REST API
* Pagination
* Improved UI/UX
* Additional automated tests

⸻

🎥 Demo Video

Demo:
https://drive.google.com/file/d/1_UIx2RI2GIn9vjqVWzZf06OIkQEGHCri/view

⸻

📄 Report

The report includes:

* Project overview
* System architecture
* Database design
* Implementation details
* Screenshots
* Testing
* Conclusion

⸻

🔗 GitHub Repository

https://github.com/YOUR_USERNAME/apple-product-catalog
