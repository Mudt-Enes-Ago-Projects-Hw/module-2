"""
Company Controller - Handles all company-related business logic
"""
from flask import request, jsonify
from src.models.company import Company
from src.config.database import db


class CompanyController:
    """Controller for company CRUD operations"""

    @staticmethod
    def get_all():
        """Get all companies"""
        companies = Company.query.order_by(Company.name).all()
        return jsonify([c.to_dict() for c in companies]), 200

    @staticmethod
    def create():
        """Create a new company"""
        data = request.get_json()
        
        # Validation
        if not data or 'name' not in data:
            return jsonify({'error': 'Name is required'}), 400
        
        if 'code' not in data:
            return jsonify({'error': 'Code is required'}), 400
        
        # Validate code format (must be 3 digits)
        code = str(data['code']).strip()
        if len(code) != 3 or not code.isdigit():
            return jsonify({'error': 'Code must be exactly 3 digits'}), 400
        
        # Check if company name or code already exists
        if Company.query.filter_by(name=data['name']).first():
            return jsonify({'error': 'Company name already exists'}), 400
        
        if Company.query.filter_by(code=code).first():
            return jsonify({'error': 'Company code already exists'}), 400
        
        # Create company
        company = Company(
            name=data['name'],
            code=code,
            description=data.get('description', '')
        )
        
        # Save to database
        db.session.add(company)
        db.session.commit()
        
        return jsonify(company.to_dict()), 201

    @staticmethod
    def get_by_id(company_id):
        """Get a single company by ID"""
        company = Company.query.get_or_404(company_id)
        return jsonify(company.to_dict()), 200

    @staticmethod
    def update(company_id):
        """Update a company (PUT)"""
        company = Company.query.get_or_404(company_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update name if provided
        if 'name' in data:
            # Check if name already exists (excluding current company)
            existing = Company.query.filter_by(name=data['name']).first()
            if existing and existing.id != company_id:
                return jsonify({'error': 'Company name already exists'}), 400
            company.name = data['name']
        
        # Update code if provided
        if 'code' in data:
            code = str(data['code']).strip()
            if len(code) != 3 or not code.isdigit():
                return jsonify({'error': 'Code must be exactly 3 digits'}), 400
            
            # Check if code already exists (excluding current company)
            existing = Company.query.filter_by(code=code).first()
            if existing and existing.id != company_id:
                return jsonify({'error': 'Company code already exists'}), 400
            company.code = code
        
        # Update description if provided
        if 'description' in data:
            company.description = data['description']
        
        from datetime import datetime
        company.updated_at = datetime.utcnow()
        
        db.session.commit()
        return jsonify(company.to_dict()), 200

    @staticmethod
    def delete(company_id):
        """Delete a company"""
        company = Company.query.get_or_404(company_id)
        
        # Check if company has associated medicines
        if company.medicines:
            return jsonify({'error': 'Cannot delete company with associated medicines'}), 400
        
        db.session.delete(company)
        db.session.commit()
        
        return '', 204
