"""
Check database tables - should only have Item and contenttypes (required by Django)
"""
import sqlite3

db_path = '/Users/enesago/Desktop/mektep/uniProjects/assignementTwoPython/backend/db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("="*50)
print("DATABASE TABLES")
print("="*50)
for table in tables:
    print(f"  - {table[0]}")

print("\n" + "="*50)
print(f"Total tables: {len(tables)}")
print("="*50)

# Show Item table structure
print("\nITEM TABLE STRUCTURE:")
print("="*50)
cursor.execute("PRAGMA table_info(items_item);")
columns = cursor.fetchall()
for col in columns:
    print(f"  {col[1]}: {col[2]}")

conn.close()
