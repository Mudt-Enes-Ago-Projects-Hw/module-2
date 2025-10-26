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
    price = db.Column(db.Float, nullable=False, default=0.0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    prescribed = db.Column(db.Boolean, nullable=False, default=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, description='', price=0.0, stock=0, prescribed=False, company_id=None):
        """Initialize medicine with unique ID"""
        if company_id is None:
            raise ValueError("company_id is required")
        
        # Get company code from database
        from src.models.company import Company
        company = Company.query.get(company_id)
        if not company:
            raise ValueError(f"Company with id {company_id} not found")
        
        self.id = self._generate_unique_id(prescribed=prescribed, company_code=company.code)
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.prescribed = prescribed
        self.company_id = company_id

    def _generate_unique_id(self, prescribed, company_code):
        """Generate a unique 11-digit ID using company code"""
        while True:
            new_id = generate_id(prescribed=prescribed, company_code=company_code)
            if not Medicine.query.filter_by(id=new_id).first():
                return new_id

    def to_dict(self):
        """Convert model to dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'prescribed': self.prescribed,
            'company_id': self.company_id,
            'company': self.company_ref.to_dict() if self.company_ref else None,
            'created_at': self.created_at.isoformat() + 'Z' if self.created_at else None,
            'updated_at': self.updated_at.isoformat() + 'Z' if self.updated_at else None
        }

    def update(self, data):
        """Update medicine with new data"""
        if 'name' in data:
            self.name = data['name']
        if 'description' in data:
            self.description = data['description']
        if 'price' in data:
            self.price = data['price']
        if 'stock' in data:
            self.stock = data['stock']
        if 'prescribed' in data:
            self.prescribed = data['prescribed']
        if 'company_id' in data:
            # Validate company exists
            from src.models.company import Company
            company = Company.query.get(data['company_id'])
            if company:
                self.company_id = data['company_id']
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f'<Medicine {self.name}>'
