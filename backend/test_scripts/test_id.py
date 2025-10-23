"""
Test script to verify the ID generation algorithm
"""
import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from algorithms.generateID import generate_id


def test_id_generation():
    print("Testing ID Generation Algorithm")
    print("-" * 50)
    
    # Generate 10 sample IDs
    ids = []
    for i in range(10):
        new_id = generate_id()
        ids.append(new_id)
        print(f"ID {i+1}: {new_id}")
    
    # Verify properties
    print("\n" + "-" * 50)
    print("Verification:")
    print(f"All IDs have 15 digits: {all(len(id) == 15 for id in ids)}")
    print(f"All IDs are numeric: {all(id.isdigit() for id in ids)}")
    print(f"All IDs are unique (in this sample): {len(ids) == len(set(ids))}")
    

if __name__ == "__main__":
    test_id_generation()
