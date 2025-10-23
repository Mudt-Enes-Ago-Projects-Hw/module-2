# Flask Pharmacy API 💊

A simple, clean Flask REST API for managing medicines with custom 15-digit ID generation.

## ✨ Features

- ✅ **CRUD Operations** - Create, Read, Update, Delete medicines
- ✅ **Custom IDs** - Random 15-digit unique identifiers
- ✅ **Search** - Search medicines by name or description
- ✅ **SQLite Database** - Lightweight, no setup required
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Pure JSON API** - No HTML, just data

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend_flask
source venv/bin/activate  # Already created!
pip install -r requirements.txt  # Already installed!
```

### 2. Run the Server

```bash
python app.py
```

Server will start at: **http://localhost:5000**

## 📡 API Endpoints

**Base URL:** `http://localhost:5000/api/medicines`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/medicines` | Get all medicines |
| `POST` | `/api/medicines` | Create a new medicine |
| `GET` | `/api/medicines/{id}` | Get a single medicine |
| `PUT` | `/api/medicines/{id}` | Full update (requires all fields) |
| `PATCH` | `/api/medicines/{id}` | Partial update |
| `DELETE` | `/api/medicines/{id}` | Delete a medicine |
| `GET` | `/api/medicines/search?q=term` | Search medicines |

## 🧪 Test the API

### Create a Medicine
```bash
curl -X POST http://localhost:5000/api/medicines \
  -H "Content-Type: application/json" \
  -d '{"name": "Aspirin", "description": "Pain reliever"}'
```

**Response:**
```json
{
  "id": "482719384756291",
  "name": "Aspirin",
  "description": "Pain reliever",
  "created_at": "2025-10-24T00:00:00Z",
  "updated_at": "2025-10-24T00:00:00Z"
}
```

### Get All Medicines
```bash
curl http://localhost:5000/api/medicines
```

### Get Single Medicine
```bash
curl http://localhost:5000/api/medicines/482719384756291
```

### Update Medicine (Full)
```bash
curl -X PUT http://localhost:5000/api/medicines/482719384756291 \
  -H "Content-Type: application/json" \
  -d '{"name": "Aspirin 500mg", "description": "Updated description"}'
```

### Update Medicine (Partial)
```bash
curl -X PATCH http://localhost:5000/api/medicines/482719384756291 \
  -H "Content-Type: application/json" \
  -d '{"name": "Aspirin 500mg"}'
```

### Delete Medicine
```bash
curl -X DELETE http://localhost:5000/api/medicines/482719384756291
```

### Search Medicines
```bash
curl "http://localhost:5000/api/medicines/search?q=aspirin"
```

## 📁 Project Structure

```
backend_flask/
├── app.py                  # Main Flask application (ALL THE CODE!)
├── algorithms/
│   ├── __init__.py
│   └── generateID.py      # 15-digit ID generator
├── pharmacy.db            # SQLite database (auto-created)
├── requirements.txt       # Python dependencies
├── venv/                  # Virtual environment
└── README.md             # This file
```

## 🎯 Why Flask?

**Compared to Django:**
- ✅ **1 file** vs 15+ files
- ✅ **~170 lines** vs 200+ lines
- ✅ **No migrations** - database auto-created
- ✅ **Easier to read** - everything in one place
- ✅ **Faster setup** - ready in minutes

## 🔧 How It Works

1. **Run `python app.py`**
2. Flask automatically creates `pharmacy.db` with the `medicine` table
3. API is ready to use immediately!

No migrations, no complex setup - just run and go! 🚀

## 📊 Database

**Table:** `medicine`

| Column | Type | Description |
|--------|------|-------------|
| `id` | String(15) | Primary key, 15-digit random number |
| `name` | String(200) | Medicine name (required) |
| `description` | Text | Medicine description (optional) |
| `created_at` | DateTime | Auto-generated timestamp |
| `updated_at` | DateTime | Auto-updated timestamp |

## 🎨 Compare with Django

### Django (backend/)
- Multiple files, folders, apps
- Migrations system required
- More configuration
- Better for large projects

### Flask (backend_flask/)
- Single `app.py` file
- No migrations needed
- Minimal configuration
- Perfect for simple APIs

**Both work great!** Choose based on your needs:
- **Simple CRUD API?** → Flask (this one!)
- **Large app with admin panel?** → Django

---

**Happy coding!** 💊🚀
