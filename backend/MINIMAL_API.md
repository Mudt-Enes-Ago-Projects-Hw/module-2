# ✅ Minimal Django REST API - Pure JSON Only

## What You Have Now

A **super minimal** Django backend that returns **pure JSON only**:

- ✅ **NO Admin Panel** - Removed
- ✅ **NO Auth Tables** - Only 4 minimal tables (down from 10+)
- ✅ **NO Browsable UI** - Only raw JSON responses
- ✅ **ONE Data Table** - `items_item` (your products)
- ✅ **Custom 15-digit IDs** - From `algorithms/generateID.py`

## Database Tables (Minimal)

```
1. items_item          ← YOUR DATA (products)
2. django_content_type ← Required by Django (tiny)
3. django_migrations   ← Tracks schema versions (tiny)
4. sqlite_sequence     ← SQLite internal (auto-increment tracking)
```

Only **1 real data table** - the rest are Django/SQLite internals.

## API Endpoints (Pure JSON)

### Base URL: `http://localhost:8000/api/items/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/items/` | Get all items (JSON array) |
| `POST` | `/api/items/` | Create new item |
| `GET` | `/api/items/{id}/` | Get single item |
| `PUT` | `/api/items/{id}/` | Full update |
| `PATCH` | `/api/items/{id}/` | Partial update |
| `DELETE` | `/api/items/{id}/` | Delete item |
| `GET` | `/api/items/search/?q=term` | Search items |

## Test the API

### Create Item
```bash
curl -X POST http://localhost:8000/api/items/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Product 1", "description": "My first product"}'
```

**Response** (pure JSON):
```json
{
  "id": "482719384756291",
  "name": "Product 1",
  "description": "My first product",
  "created_at": "2025-10-24T00:00:00Z",
  "updated_at": "2025-10-24T00:00:00Z"
}
```

### Get All Items
```bash
curl http://localhost:8000/api/items/
```

**Response**:
```json
[
  {
    "id": "482719384756291",
    "name": "Product 1",
    "description": "My first product",
    "created_at": "2025-10-24T00:00:00Z",
    "updated_at": "2025-10-24T00:00:00Z"
  }
]
```

### Update Item
```bash
curl -X PUT http://localhost:8000/api/items/482719384756291/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Product", "description": "New description"}'
```

### Delete Item
```bash
curl -X DELETE http://localhost:8000/api/items/482719384756291/
```

**Response**: `204 No Content` (empty response)

### Search Items
```bash
curl "http://localhost:8000/api/items/search/?q=product"
```

## What Was Removed

- ❌ Django Admin (`/admin/`)
- ❌ Auth tables (users, groups, permissions, sessions)
- ❌ Static files
- ❌ Templates
- ❌ CSRF middleware
- ❌ Session middleware
- ❌ Browsable API UI (HTML interface)
- ❌ Password validators

## What's Left (Minimal)

- ✅ REST Framework (JSON API)
- ✅ CORS (for frontend)
- ✅ One model: Item
- ✅ SQLite database
- ✅ Custom ID generation

## Server

**Running at:** http://127.0.0.1:8000/
**API Base:** http://127.0.0.1:8000/api/items/

No UI - pure JSON API only! 🎯
