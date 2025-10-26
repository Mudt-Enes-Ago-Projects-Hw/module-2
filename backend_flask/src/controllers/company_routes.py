"""
Company Routes
"""
from flask import Blueprint
from src.controllers.company_controller import CompanyController

# Create blueprint
company_bp = Blueprint('company', __name__, url_prefix='/api/companies')

# Routes
company_bp.route('/', methods=['GET'])(CompanyController.get_all)
company_bp.route('/', methods=['POST'])(CompanyController.create)
company_bp.route('/<int:company_id>', methods=['GET'])(CompanyController.get_by_id)
company_bp.route('/<int:company_id>', methods=['PUT'])(CompanyController.update)
company_bp.route('/<int:company_id>', methods=['DELETE'])(CompanyController.delete)
