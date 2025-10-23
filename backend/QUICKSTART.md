# Django Backend - Quick Start Guide

## ✅ What's Been Created

Your Django backend is now set up with:

### 📁 Project Structure
```
backend/
├── algorithms/
│   ├── __init__.py
│   └── generateID.py          # 15-digit random ID generator
├── config/                    # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── items/                     # Items CRUD app
│   ├── models.py             # Item model with custom ID
│   ├── serializers.py        # REST API serializers
│   ├── views.py              # CRUD endpoints
│   ├── urls.py               # API routes
│   └── admin.py              # Admin panel configuration
├── db.sqlite3                # SQLite database
├── manage.py
├── requirements.txt
├── test_api.py               # API testing script
└── test_id.py                # ID generation test
```

### 🎯 Features Implemented

✅ **Custom ID Generation**: Random 15-digit numbers via `algorithms/generateID.py`
✅ **SQLite Database**: Already migrated and ready to use
✅ **CRUD Operations**:
   - Create items (POST)
   - Read items (GET)
   - Update items (PUT/PATCH)
   - Delete items (DELETE)
   - Search items (GET with query params)

✅ **API Endpoints**:
   - `POST /api/items/` - Create item
   - `GET /api/items/` - List all items
   - `GET /api/items/{id}/` - Get specific item
   - `PUT /api/items/{id}/` - Full update
   - `PATCH /api/items/{id}/` - Partial update
   - `DELETE /api/items/{id}/` - Delete item
   - `GET /api/items/search/?q=term` - Search items

✅ **CORS Enabled**: Frontend at localhost:3000 can access the API
✅ **Admin Panel**: Available at http://localhost:8000/admin/

## 🚀 How to Use

### 1. Start the Server
The server is already running at `http://127.0.0.1:8000/`

To restart it later:
```bash
cd backend
source venv/bin/activate  # or use full path to python
python manage.py runserver
```

### 2. Test the API

**Option 1: Use the test script**
```bash
cd backend
pip install requests  # if not already installed
python test_api.py
```

**Option 2: Use curl**
```bash
# Create an item
curl -X POST http://localhost:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "My Item", "description": "Test item"}'

# Get all items
curl http://localhost:8000/api/items/

# Search items
curl http://localhost:8000/api/items/search/?q=test

# Get specific item (use actual ID)
curl http://localhost:8000/api/items/123456789012345/

# Update item
curl -X PUT http://localhost:8000/api/items/123456789012345/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated", "description": "New desc"}'

# Delete item
curl -X DELETE http://localhost:8000/api/items/123456789012345/
```

**Option 3: Use the browsable API**
Just visit http://localhost:8000/api/items/ in your browser!

### 3. Access Admin Panel

First, create a superuser:
```bash
cd backend
source venv/bin/activate
python manage.py createsuperuser
```

Then visit: http://localhost:8000/admin/

## 📊 Example API Usage

### Create Item
```bash
POST /api/items/
{
  "name": "Sample Item",
  "description": "This is a test"
}

Response (201 Created):
{
  "id": "847392018475629",
  "name": "Sample Item",
  "description": "This is a test",
  "created_at": "2025-10-24T00:30:00Z",
  "updated_at": "2025-10-24T00:30:00Z"
}
```

### Search Items
```bash
GET /api/items/search/?q=sample

Response (200 OK):
[
  {
    "id": "847392018475629",
    "name": "Sample Item",
    "description": "This is a test",
    "created_at": "2025-10-24T00:30:00Z",
    "updated_at": "2025-10-24T00:30:00Z"
  }
]
```

## 🔧 ID Generation Algorithm

The custom ID generator in `algorithms/generateID.py`:
- Generates random 15-digit numbers
- Range: 100000000000000 to 999999999999999
- Ensures uniqueness before saving
- Used automatically when creating new items

## 📝 Notes

- The server is currently running in development mode
- CORS is configured for `http://localhost:3000` (your frontend)
- All data is stored in `db.sqlite3`
- Virtual environment is located in `backend/venv/`

## 🎉 You're All Set!

The backend is running and ready to be integrated with your frontend!
