# Django Backend - Simple CRUD API

A simple Django REST API with CRUD operations for items, using a custom 15-digit ID generation algorithm.

## Features

- **Create** items (POST)
- **Read** items (GET)
- **Update** items (PUT/PATCH)
- **Delete** items (DELETE)
- **Search** items by name or description
- Custom 15-digit random ID generation
- SQLite database
- CORS enabled for frontend integration

## Setup Instructions

1. **Navigate to the backend folder**:
   ```bash
   cd backend
   ```

2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin panel)**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Items CRUD Operations

- **GET** `/api/items/` - List all items
- **POST** `/api/items/` - Create a new item
- **GET** `/api/items/{id}/` - Get a specific item
- **PUT** `/api/items/{id}/` - Update an item (full update)
- **PATCH** `/api/items/{id}/` - Partial update an item
- **DELETE** `/api/items/{id}/` - Delete an item
- **GET** `/api/items/search/?q=search_term` - Search items

### Request/Response Examples

**POST /api/items/**
```json
{
  "name": "Sample Item",
  "description": "This is a sample item"
}
```

**Response:**
```json
{
  "id": "123456789012345",
  "name": "Sample Item",
  "description": "This is a sample item",
  "created_at": "2025-10-24T12:00:00Z",
  "updated_at": "2025-10-24T12:00:00Z"
}
```

## Project Structure

```
backend/
├── algorithms/
│   ├── __init__.py
│   └── generateID.py      # Custom 15-digit ID generation
├── config/                # Django project settings
│   ├── settings.py
│   └── urls.py
├── items/                 # Items app
│   ├── models.py         # Item model
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   └── urls.py           # API routes
├── manage.py
└── requirements.txt
```

## Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/` after creating a superuser.
