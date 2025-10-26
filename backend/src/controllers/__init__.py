"""
Controllers package
"""
from .medicine import MedicineController, medicine_bp
from .company import CompanyController, company_bp

__all__ = ['MedicineController', 'medicine_bp', 'CompanyController', 'company_bp']
