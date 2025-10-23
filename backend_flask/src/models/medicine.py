"""
Medicine Model
"""
from datetime import datetime
from src.config.database import db
from algorithms.generateID import generate_id


class Medicine(db.Model):
    """Medicine model with custom 15-digit ID"""
    __tablename__ = 'medicine'
    
    id = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, description=''):
        """Initialize medicine with unique ID"""
        self.id = self._generate_unique_id()
        self.name = name
        self.description = description

    def _generate_unique_id(self):
        """Generate a unique 15-digit ID"""
        while True:
            new_id = generate_id()
            if not Medicine.query.filter_by(id=new_id).first():
                return new_id

    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat() + 'Z' if self.created_at else None,
            'updated_at': self.updated_at.isoformat() + 'Z' if self.updated_at else None
        }

    def update(self, data):
        """Update medicine with new data"""
        if 'name' in data:
            self.name = data['name']
        if 'description' in data:
            self.description = data['description']
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f'<Medicine {self.name}>'
