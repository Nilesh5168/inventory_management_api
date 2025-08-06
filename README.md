# inventory_management_api

A simple RESTful API for managing inventory, built with **FastAPI**, **SQLAlchemy**, and **Alembic**.  
Supports products and stock transactions with CRUD operations and tracking.

---

## 🚀 Features

- Add, list, update, delete products
- Track stock-in and stock-out transactions
- PostgreSQL database integration
- Automatic schema migrations using Alembic
- Interactive API docs at `/docs`

---

## 🛠️ Setup Instructions

1. Create a virtual environment  
`python -m venv venv`

2. Activate the virtual environment (on Windows)  
`venv\Scripts\activate`

3. Install required packages  
`pip install -r requirements.txt`

4. Set your PostgreSQL URL in `alembic.ini`  
Example:  
`sqlalchemy.url = postgresql://username:password@localhost:5432/inventory_new`

5. Run Alembic migrations  
`alembic upgrade head`

6. Start the FastAPI server  
`uvicorn main:app --reload`

7. Visit interactive docs  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Sample API Requests

🔹 Add a Product (`POST /products/`)

Body-
{
  "name": "Notebook",
  "description": "200 pages",
  "price": 35.5,
  "available_quantity": 50
}



🔹 List All Products (GET /products/)
🔹 Get Product by ID (GET /products/1)

🔹 Update Product (PUT /products/1)

Body-
{
  "name": "Notebook",
  "description": "Updated 250 pages",
  "price": 40.0,
  "available_quantity": 60
}

🔹 Delete Product (DELETE /products/1)

🔹 Add Stock Transaction (POST /stock/)

Body-
{
  "product_id": 1,
  "quantity": 20,
  "transaction_type": "IN"
}
transaction_type must be either "IN" or "OUT"



## ✅ Postman Testing Guide — Inventory API

📌 Base URL:
http://127.0.0.1:8000

1. Add a Product

Method: POST

URL: /products/

Body (raw, JSON):
{
  "name": "Notebook",
  "description": "200 pages",
  "price": 50.0,
  "available_quantity": 100
}

2. Get All Products

Method: GET

URL: /products/

Body: None

3. Get Product by ID

Method: GET

URL: /products/1

Replace 1 with the actual product ID

4. Update a Product

Method: PUT

URL: /products/1

Body (raw, JSON):

{
  "name": "Notebook - Updated",
  "description": "250 pages",
  "price": 55.0,
  "available_quantity": 120
}

5. Delete a Product

Method: DELETE

URL: /products/1

Replace 1 with the product ID

Body: None

6. Add a Stock Transaction

Method: POST

URL: /stock/

Body (raw, JSON):

{
  "product_id": 1,
  "quantity": 10,
  "transaction_type": "IN"
}

Allowed transaction_type values:

"IN" — to add stock

"OUT" — to remove stock

## ✅ Notes

Ensure your PostgreSQL user has CREATE privileges on the public schema.

Alembic revision files are committed in /alembic/versions/.

## 📧 Contact
Developer: Nilesh Patil
Email: nileshpatil5168@gmail.com
