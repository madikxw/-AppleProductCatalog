Apple Product Catalog

A Flask-based web application for browsing and managing a catalogue of Apple products with search, filtering, sorting, and full CRUD operations.

Educational Practice Project · Astana IT University · 2026

⸻

Student Information

Field	Details
Student	Bissentayev Madiyar
Academic Group	First Year · Web Development
Project Type	Individual Educational Practice Project
Project Topic	Apple Product Catalog — E-commerce Catalogue Management System

⸻

Project Description

The Apple Product Catalog is a full-stack web application that demonstrates the fundamentals of web development using Python, Flask, and SQLite. The application follows a three-layer architecture:

* Presentation Layer: Jinja2 templates with Bootstrap 5 for a responsive and user-friendly interface.
* Application Layer: Flask routes handling HTTP requests and business logic.
* Data Layer: SQLite database using parameterized SQL queries for secure data access.

Core Features

1. Browse all Apple products.
2. Search products by name and description.
3. Filter products by category.
4. Sort products by price.
5. View detailed information about each product.
6. Add new products.
7. Edit existing products.
8. Delete products with confirmation.
9. Store all data in a SQLite database.

⸻

Technology Stack

* Python 3
* Flask
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* Jinja2
* pytest
* Git & GitHub
* GitHub Actions

⸻

How to Run

Prerequisites

* Python 3.7 or newer
* pip

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/apple-product-catalog.git
cd apple-product-catalog

Install dependencies:

pip install -r requirements.txt

Initialize the database:

python src/init_db.py

Run the application:

python src/app.py

Open your browser:

http://127.0.0.1:5000

⸻

Project Structure

(Add your project structure image here.)

⸻

Features

Search & Filter

* Search products by both name and description.
* Filter products by category.
* Sort products by price.
* Combine search, filter, and sorting in a single request.

CRUD Operations

* Add new products.
* Edit existing products.
* Delete products using a confirmation dialog.
* View detailed product information.

Database

The application uses SQLite.

Table:

products

Columns:

* id
* name
* description
* price
* category
* image_url

The database contains 25 sample Apple products.

⸻

Architecture

(Add your architecture diagram here.)

⸻

Running Tests

Run:

pytest tests/

The automated tests verify:

* Repository structure
* Application functionality
* CRUD operations

⸻

Development Challenges

During development I encountered several challenges:

* Learning Flask and understanding request routing.
* Designing the SQLite database.
* Integrating the backend with Jinja2 templates.
* Implementing search, filtering, and sorting using SQL queries.
* Configuring GitHub Actions for automated checks.
* Testing the application and fixing discovered issues.

⸻

Future Improvements

* User authentication.
* Role-based authorization.
* Pagination.
* Better UI/UX.
* SQLAlchemy ORM.
* REST API.
* More automated tests.

⸻

Demo Video

The demonstration video presents the application, explains its features, and shows the implementation of CRUD operations, search, filtering, and sorting.

Demo Link:

Replace with your Google Drive or YouTube link.

⸻

Report

The project report includes:

* Project overview
* Problem statement
* Technologies used
* Database design
* Application architecture
* Implementation details
* Screenshots
* Testing
* Conclusion

⸻

GitHub Repository

Repository:

https://github.com/YOUR_USERNAME/apple-product-catalog
