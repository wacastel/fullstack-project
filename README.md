# Full-Stack Item Manager: FastAPI + Django

This project demonstrates a microservices-style architecture using a high-performance FastAPI backend for data management and a Django frontend for the user interface.

## 🏗️ Architecture Overview

- Backend Server: Built with FastAPI and SQLAlchemy. It handles all database operations CRUD and exposes a RESTful API. It uses a lightweight SQLite database \`items\.db\`.
- Frontend Client: Built with Django. It does not use its own database models for items; instead, it consumes the FastAPI endpoints via the `requests` library to render HTML templates to the user.

## 📂 Directory Structure

```text
my_fullstack_project/
├── fastapi_server/           # Backend Code
│   ├── server.py             # FastAPI application and SQLAlchemy models
│   └── items.db              # SQLite database auto\-generated
│
└── django_client/            # Frontend Code
    ├── manage.py             # Django entry point
    ├── client_project/       # Main Django project settings
    └── items_app/            # Django app for item management
    ├── views.py              # Relays requests to FastAPI
    ├── urls.py               # App routing
    └── templates/            # HTML Templates
    └── items/
    ├── list.html
    ├── form.html
    └── confirm_delete.html
```

## 🛠️ Prerequisites

Ensure you have Python 3.8+ installed. It is highly recommended to use a virtual environment.

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required dependencies for both services:

```bash
pip install fastapi uvicorn sqlalchemy django requests
```

## 🚀 Running the Application

Because this project consists of two separate services, you will need to run them in two separate terminal windows.

### 1. Start the FastAPI Backend
Open a terminal and navigate to the `fastapi_server` directory:

```bash
cd fastapi_server
uvicorn server:app --reload
```
*The API will be available at `http://127.0.0.1:8000`.*
*Interactive API documentation SwaggerUI is available at `http://127.0.0.1:8000/docs`.*

### 2. Start the Django Frontend
Open a second terminal window and navigate to the `django_client` directory:

```bash
cd django_client
python manage.py runserver 8080
```
*The web interface will be available at `http://127.0.0.1:8080/items/`.*

## 🔌 API Endpoints

The FastAPI backend exposes the following RESTful endpoints:

| Method | Endpoint          | Description               |
|--------|--------------------|---------------------------|
| GET    | `/items/`         | Retrieve all items        |
| GET    | `/items/{id}`     | Retrieve a specific item  |
| POST   | `/items/`         | Create a new item         |
| PUT    | `/items/{id}`     | Update an existing item   |
| DELETE | `/items/{id}`     | Delete an item            |

## 📝 Usage

1. Open `http://127.0.0.1:8080/items/` in your web browser.
2. Click Create New Item to add data. This will send a POST request to the FastAPI server.
3. View the list of items, which are fetched in real-time from the backend.
4. Use the Edit and Delete links to manage your entries.
