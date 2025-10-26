# Flask Pharmacy API 💊

A clean Flask REST API for managing medicines and pharmaceutical companies with custom ID generation.

## ✨ Features

- ✅ **CRUD Operations** - Complete medicine and company management
- ✅ **Custom IDs** - 11-digit unique identifiers with checksum validation
- ✅ **Company System** - Dynamic company management with 3-digit codes
- ✅ **Search** - Search medicines by name or description
- ✅ **SQLite Database** - Lightweight, auto-created on first run
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **Pure JSON API** - RESTful design

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
cd backend_flask
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python app.py
```

Server will start at: **http://localhost:3001**

On first run, the database will be created and seeded with initial companies:
- Acme Pharma (101)
- HealthPlus Labs (102)
- Pharmatech (103)
- Medicore (104)

## 📡 API Endpoints

### Medicine Endpoints

**Base URL:** `http://localhost:3001/api/medicines`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/medicines` | Get all medicines |
| `POST` | `/api/medicines` | Create a new medicine |
| `GET` | `/api/medicines/{id}` | Get a single medicine |
| `PUT` | `/api/medicines/{id}` | Update a medicine |
| `DELETE` | `/api/medicines/{id}` | Delete a medicine |
| `GET` | `/api/medicines/search?q=term` | Search medicines |

### Company Endpoints

**Base URL:** `http://localhost:3001/api/companies`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/companies` | Get all companies |
| `POST` | `/api/companies` | Create a new company |
| `GET` | `/api/companies/{id}` | Get a single company |
| `PUT` | `/api/companies/{id}` | Update a company |
| `DELETE` | `/api/companies/{id}` | Delete a company |

## 🧪 API Examples

### Company Operations

#### Get All Companies
```bash
curl http://localhost:3001/api/companies
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Acme Pharma",
    "code": "101",
    "description": "Leading pharmaceutical company",
    "created_at": "2025-10-26T12:00:00Z",
    "updated_at": "2025-10-26T12:00:00Z"
  }
]
```

#### Create a New Company
```bash
curl -X POST http://localhost:3001/api/companies \
  -H "Content-Type: application/json" \
  -d '{
    "name": "BioMed Corp",
    "code": "105",
    "description": "Biomedical research and development"
  }'
```

#### Get Company by ID
```bash
curl http://localhost:3001/api/companies/1
```

#### Update a Company
```bash
curl -X PUT http://localhost:3001/api/companies/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Acme Pharma Updated",
    "description": "Updated description"
  }'
```

#### Delete a Company
```bash
curl -X DELETE http://localhost:3001/api/companies/5
```

### Medicine Operations

#### Create a Medicine
```bash
curl -X POST http://localhost:3001/api/medicines \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Aspirin Plus",
    "description": "Pain relief medication",
    "price": 12.99,
    "stock": 100,
    "prescribed": false,
    "company_id": 1
  }'
```

**Response:**
```json
{
  "id": "10151905730",
  "name": "Aspirin Plus",
  "description": "Pain relief medication",
  "price": 12.99,
  "stock": 100,
  "prescribed": false,
  "company_id": 1,
  "company": {
    "id": 1,
    "name": "Acme Pharma",
    "code": "101",
    "description": "Leading pharmaceutical company"
  },
  "created_at": "2025-10-26T12:00:00Z",
  "updated_at": "2025-10-26T12:00:00Z"
}
```

#### Get All Medicines
```bash
curl http://localhost:3001/api/medicines
```

#### Get Single Medicine by ID
```bash
curl http://localhost:3001/api/medicines/10151905730
```

#### Update Medicine
```bash
curl -X PUT http://localhost:3001/api/medicines/10151905730 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Aspirin Plus 500mg",
    "description": "Enhanced pain relief",
    "price": 15.99,
    "stock": 150,
    "company_id": 1
  }'
```

#### Delete Medicine
```bash
curl -X DELETE http://localhost:3001/api/medicines/10151905730
```

#### Search Medicines
```bash
curl "http://localhost:3001/api/medicines/search?q=aspirin"
```

## 📁 Project Structure

```
backend_flask/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── test_company_system.py         # Test script for company system
├── algorithms/
│   ├── __init__.py
│   ├── generateID.py              # 11-digit ID generator with checksum
│   ├── verifyID.py                # ID verification
│   └── testID.py                  # Algorithm tests
├── instance/
│   └── pharmacy.db                # SQLite database (auto-created)
└── src/
    ├── config/
    │   ├── settings.py            # App configuration
    │   └── database.py            # Database setup
    ├── models/
    │   ├── medicine.py            # Medicine model
    │   └── company.py             # Company model
    └── controllers/
        ├── medicine_controller.py  # Medicine business logic
        ├── medicine_routes.py      # Medicine API routes
        ├── company_controller.py   # Company business logic
        └── company_routes.py       # Company API routes
```

## 📊 Database Schema

### Company Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key (auto-increment) |
| `name` | String(100) | Unique company name |
| `code` | String(3) | Unique 3-digit code (e.g., "101") |
| `description` | Text | Company description |
| `created_at` | DateTime | Creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

### Medicine Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | String(15) | Primary key, 11-digit ID with checksum |
| `name` | String(200) | Medicine name |
| `description` | Text | Medicine description |
| `price` | Float | Price |
| `stock` | Integer | Stock quantity |
| `prescribed` | Boolean | Requires prescription? |
| `company_id` | Integer | Foreign key to Company |
| `created_at` | DateTime | Creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

## 🔐 Medicine ID Format

Each medicine ID is an 11-digit number composed of two checksum-validated segments:

- **Segment A (4 digits)**: `[Company Code (3 digits)][Checksum (1 digit)]`
- **Segment B (7 digits)**: `[Prescribed Flag (1)][Random (5)][Checksum (1)]`

Example: `10151905730`
- `1015` = Acme Pharma (101) + checksum (5)
- `1905730` = Prescribed (1) + random + checksum (0)

## 🔧 Technologies

- **Flask 3.1.2** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database
- **Flask-CORS 6.0.1** - Cross-origin resource sharing
- **python-dotenv 1.0.0** - Environment variables
- **SQLite** - Database

## 🧪 Testing

Run the test script to see the system in action:

```bash
python3 test_company_system.py
```

This demonstrates:
- Listing seeded companies
- Creating new companies
- Creating medicines with different companies
- Dynamic ID generation with company codes

---

**Happy coding!** 💊🚀
