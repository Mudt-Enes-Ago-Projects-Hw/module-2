"""
API Testing Script
Test all CRUD operations for the Items API
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/items/"

def print_response(response, operation):
    print(f"\n{'='*60}")
    print(f"{operation}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")

def test_api():
    print("Testing Django CRUD API")
    
    # 1. CREATE - POST request
    print("\n1. CREATE - Creating a new item...")
    new_item = {
        "name": "Test Item 1",
        "description": "This is a test item created via API"
    }
    response = requests.post(BASE_URL, json=new_item)
    print_response(response, "CREATE Item")
    
    if response.status_code == 201:
        item_id = response.json()['id']
        print(f"\n✓ Item created with ID: {item_id}")
        
        # 2. READ - GET single item
        print("\n2. READ - Getting the created item...")
        response = requests.get(f"{BASE_URL}{item_id}/")
        print_response(response, "GET Single Item")
        
        # 3. UPDATE - PUT request
        print("\n3. UPDATE - Updating the item...")
        updated_item = {
            "name": "Updated Test Item",
            "description": "This item has been updated"
        }
        response = requests.put(f"{BASE_URL}{item_id}/", json=updated_item)
        print_response(response, "UPDATE Item (PUT)")
        
        # 4. PARTIAL UPDATE - PATCH request
        print("\n4. PARTIAL UPDATE - Patching the item...")
        patch_data = {
            "description": "Partially updated description"
        }
        response = requests.patch(f"{BASE_URL}{item_id}/", json=patch_data)
        print_response(response, "PARTIAL UPDATE (PATCH)")
    
    # 5. CREATE more items for list/search
    print("\n5. Creating more items for testing list and search...")
    items = [
        {"name": "Apple", "description": "A red fruit"},
        {"name": "Banana", "description": "A yellow fruit"},
        {"name": "Orange", "description": "A citrus fruit"},
    ]
    
    created_ids = []
    for item in items:
        response = requests.post(BASE_URL, json=item)
        if response.status_code == 201:
            created_ids.append(response.json()['id'])
    
    print(f"✓ Created {len(created_ids)} additional items")
    
    # 6. LIST - GET all items
    print("\n6. LIST - Getting all items...")
    response = requests.get(BASE_URL)
    print_response(response, "LIST All Items")
    
    # 7. SEARCH - Search for items
    print("\n7. SEARCH - Searching for 'fruit'...")
    response = requests.get(f"{BASE_URL}search/", params={"q": "fruit"})
    print_response(response, "SEARCH Items")
    
    # 8. DELETE - Delete an item
    if created_ids:
        print(f"\n8. DELETE - Deleting item {created_ids[0]}...")
        response = requests.delete(f"{BASE_URL}{created_ids[0]}/")
        print_response(response, "DELETE Item")
        
        # Verify deletion
        print(f"\nVerifying deletion...")
        response = requests.get(f"{BASE_URL}{created_ids[0]}/")
        if response.status_code == 404:
            print("✓ Item successfully deleted (404 Not Found)")
        else:
            print("✗ Item still exists")
    
    print("\n" + "="*60)
    print("API Testing Complete!")
    print("="*60)

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API server.")
        print("Make sure the Django server is running: python manage.py runserver")
    except Exception as e:
        print(f"Error: {e}")
