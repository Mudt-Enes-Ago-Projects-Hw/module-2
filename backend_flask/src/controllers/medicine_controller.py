"""
Medicine Controller - Handles all medicine-related business logic
"""
from flask import request, jsonify
from src.models.medicine import Medicine
from src.config.database import db


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
        
        # Create medicine
        medicine = Medicine(
            name=data['name'],
            description=data.get('description', '')
        )
        
        # Save to database
        db.session.add(medicine)
        db.session.commit()
        
        return jsonify(medicine.to_dict()), 201

    @staticmethod
    def get_by_id(medicine_id):
        """Get a single medicine by ID"""
        medicine = Medicine.query.get_or_404(medicine_id)
        return jsonify(medicine.to_dict()), 200

    @staticmethod
    def update(medicine_id):
        """Full update of a medicine (PUT)"""
        medicine = Medicine.query.get_or_404(medicine_id)
        data = request.get_json()
        
        # Validation
        if not data or 'name' not in data:
            return jsonify({'error': 'Name is required'}), 400
        
        # Update all fields
        medicine.update({
            'name': data['name'],
            'description': data.get('description', '')
        })
        
        db.session.commit()
        return jsonify(medicine.to_dict()), 200

    @staticmethod
    def partial_update(medicine_id):
        """Partial update of a medicine (PATCH)"""
        medicine = Medicine.query.get_or_404(medicine_id)
        data = request.get_json()
        
        # Update only provided fields
        medicine.update(data)
        
        db.session.commit()
        return jsonify(medicine.to_dict()), 200

    @staticmethod
    def delete(medicine_id):
        """Delete a medicine"""
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
