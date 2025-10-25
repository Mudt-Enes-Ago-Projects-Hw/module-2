# Pharmacy API Backend# Flask Pharmacy API 💊



A simple Flask REST API for managing pharmacy medicines with CRUD operations.A simple, clean Flask REST API for managing medicines with custom 15-digit ID generation.



## 🚀 Quick Start## ✨ Features



### 1. Install Dependencies- ✅ **CRUD Operations** - Create, Read, Update, Delete medicines

- ✅ **Custom IDs** - Random 15-digit unique identifiers

```bash- ✅ **Search** - Search medicines by name or description

cd backend_flask- ✅ **SQLite Database** - Lightweight, no setup required

pip install -r requirements.txt- ✅ **CORS Enabled** - Ready for frontend integration

```- ✅ **Pure JSON API** - No HTML, just data



### 2. Configure Environment## 🚀 Quick Start



Copy `.env.example` to `.env`:### 1. Install Dependencies



```bash```bash

cp .env.example .envcd backend_flask

```source venv/bin/activate  # Already created!

pip install -r requirements.txt  # Already installed!

Edit `.env` to change settings (optional):```



```bash### 2. Run the Server

PORT=3001

FLASK_ENV=development```bash

```python app.py

```

### 3. Run the Server

Server will start at: **http://localhost:3001**

```bash

./venv/bin/python3 app.py## 📡 API Endpoints

```

**Base URL:** `http://localhost:3001/api/medicines`

The API will be available at: **http://localhost:3001/api/medicines**

| Method | Endpoint | Description |

## 📡 API Endpoints|--------|----------|-------------|

| `GET` | `/api/medicines` | Get all medicines |

| Method | Endpoint | Description || `POST` | `/api/medicines` | Create a new medicine |

|--------|----------|-------------|| `GET` | `/api/medicines/{id}` | Get a single medicine |

| GET | `/api/medicines` | Get all medicines || `PUT` | `/api/medicines/{id}` | Full update (requires all fields) |

| POST | `/api/medicines` | Create a new medicine || `PATCH` | `/api/medicines/{id}` | Partial update |

| GET | `/api/medicines/{id}` | Get a specific medicine || `DELETE` | `/api/medicines/{id}` | Delete a medicine |

| PUT | `/api/medicines/{id}` | Update a medicine || `GET` | `/api/medicines/search?q=term` | Search medicines |

| DELETE | `/api/medicines/{id}` | Delete a medicine |

| GET | `/api/medicines/search?q=term` | Search medicines |## 🧪 Test the API



## 📝 Example Usage### Create a Medicine

```bash

### Create a Medicinecurl -X POST http://localhost:3001/api/medicines \

  -H "Content-Type: application/json" \

```bash  -d '{"name": "Aspirin", "description": "Pain reliever"}'

curl -X POST http://localhost:3001/api/medicines \```

  -H "Content-Type: application/json" \

  -d '{"name": "Aspirin", "description": "Pain reliever"}'**Response:**

``````json

{

### Get All Medicines  "id": "482719384756291",

  "name": "Aspirin",

```bash  "description": "Pain reliever",

curl http://localhost:3001/api/medicines  "created_at": "2025-10-24T00:00:00Z",

```  "updated_at": "2025-10-24T00:00:00Z"

}

### Update a Medicine```



```bash### Get All Medicines

curl -X PUT http://localhost:3001/api/medicines/{id} \```bash

  -H "Content-Type: application/json" \curl http://localhost:3001/api/medicines

  -d '{"name": "Aspirin 500mg", "description": "Updated description"}'```

```

### Get Single Medicine

### Delete a Medicine```bash

curl http://localhost:3001/api/medicines/482719384756291

```bash```

curl -X DELETE http://localhost:3001/api/medicines/{id}

```### Update Medicine (Full)

```bash

### Search Medicinescurl -X PUT http://localhost:3001/api/medicines/482719384756291 \

  -H "Content-Type: application/json" \

```bash  -d '{"name": "Aspirin 500mg", "description": "Updated description"}'

curl http://localhost:3001/api/medicines/search?q=Aspirin```

```

### Update Medicine (Partial)

## 🗂️ Project Structure```bash

curl -X PATCH http://localhost:3001/api/medicines/482719384756291 \

```  -H "Content-Type: application/json" \

backend_flask/  -d '{"name": "Aspirin 500mg"}'

├── app.py                      # Main application entry point```

├── requirements.txt            # Python dependencies

├── .env                        # Environment variables (not in git)### Delete Medicine

├── .env.example               # Example environment variables```bash

├── algorithms/curl -X DELETE http://localhost:3001/api/medicines/482719384756291

│   └── generateID.py          # 15-digit ID generator```

└── src/

    ├── config/### Search Medicines

    │   ├── settings.py        # App configuration```bash

    │   └── database.py        # Database setupcurl "http://localhost:3001/api/medicines/search?q=aspirin"

    ├── models/```

    │   └── medicine.py        # Medicine model

    └── controllers/## 📁 Project Structure

        ├── medicine_controller.py  # Business logic

        └── medicine_routes.py      # API routes```

```backend_flask/

├── app.py                  # Main Flask application (ALL THE CODE!)

## 🔧 Technologies├── algorithms/

│   ├── __init__.py

- **Flask 3.1.2** - Web framework│   └── generateID.py      # 15-digit ID generator

- **Flask-SQLAlchemy 3.1.1** - ORM for database├── pharmacy.db            # SQLite database (auto-created)

- **Flask-CORS 6.0.1** - Cross-origin resource sharing├── requirements.txt       # Python dependencies

- **python-dotenv 1.0.0** - Environment variable management├── venv/                  # Virtual environment

- **SQLite** - Database└── README.md             # This file

```

## 📦 Features

## 🎯 Why Flask?

- ✅ Clean MVC architecture

- ✅ Custom 15-digit ID generation**Compared to Django:**

- ✅ RESTful API design- ✅ **1 file** vs 15+ files

- ✅ CORS enabled for frontend integration- ✅ **~170 lines** vs 200+ lines

- ✅ Environment-based configuration- ✅ **No migrations** - database auto-created

- ✅ Search functionality- ✅ **Easier to read** - everything in one place

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
