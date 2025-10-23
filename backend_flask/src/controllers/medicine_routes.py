"""
Medicine Routes - URL endpoints
"""
from flask import Blueprint
from src.controllers.medicine_controller import MedicineController

# Create blueprint
medicine_bp = Blueprint('medicines', __name__, url_prefix='/api/medicines')

# Routes
@medicine_bp.route('', methods=['GET'])
def get_medicines():
    """GET /api/medicines - Get all medicines"""
    return MedicineController.get_all()


@medicine_bp.route('', methods=['POST'])
def create_medicine():
    """POST /api/medicines - Create a new medicine"""
    return MedicineController.create()


@medicine_bp.route('/<medicine_id>', methods=['GET'])
def get_medicine(medicine_id):
    """GET /api/medicines/{id} - Get a single medicine"""
    return MedicineController.get_by_id(medicine_id)


@medicine_bp.route('/<medicine_id>', methods=['PUT'])
def update_medicine(medicine_id):
    """PUT /api/medicines/{id} - Update medicine"""
    return MedicineController.update(medicine_id)


@medicine_bp.route('/<medicine_id>', methods=['DELETE'])
def delete_medicine(medicine_id):
    """DELETE /api/medicines/{id} - Delete medicine"""
    return MedicineController.delete(medicine_id)


@medicine_bp.route('/search', methods=['GET'])
def search_medicines():
    """GET /api/medicines/search?q=term - Search medicines"""
    return MedicineController.search()
