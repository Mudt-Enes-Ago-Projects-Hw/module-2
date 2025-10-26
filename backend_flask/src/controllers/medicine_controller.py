"""
Medicine Controller - Handles all medicine-related business logic
"""
from flask import request, jsonify
from src.models.medicine import Medicine
from src.config.database import db
from algorithms.verifyID import verify_id


class MedicineController:
    """Controller for medicine CRUD operations"""

    @staticmethod
    def get_all():
        """Get all medicines"""
        medicines = Medicine.query.order_by(Medicine.created_at.desc()).all()
        return jsonify([m.to_dict() for m in medicines]), 200

    @staticmethod
    def create():
        """Create a new medicine"""
        data = request.get_json()
        
        # Validation
        if not data or 'name' not in data:
            return jsonify({'error': 'Name is required'}), 400
        
        if 'company_id' not in data:
            return jsonify({'error': 'Company ID is required'}), 400
        
        try:
            # Create medicine
            medicine = Medicine(
                name=data['name'],
                description=data.get('description', ''),
                price=data.get('price', 0.0),
                stock=data.get('stock', 0),
                prescribed=data.get('prescribed', False),
                company_id=data['company_id']
            )
            
            # Save to database
            db.session.add(medicine)
            db.session.commit()
            
            return jsonify(medicine.to_dict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    @staticmethod
    def get_by_id(medicine_id):
        """Get a single medicine by ID"""

        # Validate the ID format and checksum
        if not verify_id(medicine_id):
            return jsonify({'error': 'Invalid or mistyped ID'}), 400
        
        medicine = Medicine.query.get_or_404(medicine_id)
        return jsonify(medicine.to_dict()), 200

    @staticmethod
    def update(medicine_id):
        """Update a medicine (PUT)"""
        medicine = Medicine.query.get_or_404(medicine_id)
        data = request.get_json()

        # Validate the ID format and checksum
        if not verify_id(medicine_id):
            return jsonify({'error': 'Invalid or mistyped ID'}), 400
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Update only provided fields
        medicine.update(data)
        
        db.session.commit()
        return jsonify(medicine.to_dict()), 200

    @staticmethod
    def delete(medicine_id):
        """Delete a medicine"""

        # Validate the ID format and checksum
        if not verify_id(medicine_id):
            return jsonify({'error': 'Invalid or mistyped ID'}), 400

        medicine = Medicine.query.get_or_404(medicine_id)
        
        db.session.delete(medicine)
        db.session.commit()
        
        return '', 204

    @staticmethod
    def search():
        """Search medicines by name or description"""
        query = request.args.get('q', '')
        
        if query:
            medicines = Medicine.query.filter(
                (Medicine.name.contains(query)) | 
                (Medicine.description.contains(query))
            ).order_by(Medicine.created_at.desc()).all()
        else:
            medicines = Medicine.query.order_by(Medicine.created_at.desc()).all()
        
        return jsonify([m.to_dict() for m in medicines]), 200
