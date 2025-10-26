"""
Company Model
"""
from datetime import datetime
from src.config.database import db


class Company(db.Model):
    """Company model for medicine manufacturers"""
    __tablename__ = 'company'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)  # 3-digit code
    description = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with medicines
    medicines = db.relationship('Medicine', backref='company_ref', lazy=True)

    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'created_at': self.created_at.isoformat() + 'Z' if self.created_at else None,
            'updated_at': self.updated_at.isoformat() + 'Z' if self.updated_at else None
        }

    def __repr__(self):
        return f'<Company {self.name} ({self.code})>'
