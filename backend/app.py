"""
Flask Pharmacy API - Clean Architecture
Main application entry point
"""
from flask import Flask, jsonify
from flask_cors import CORS
from src.config.settings import config
from src.config.database import db
from src.controllers.medicine import medicine_bp
from src.controllers.company import company_bp


def create_app():
    """Application factory pattern"""
    # Initialize Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, origins=config.CORS_ORIGINS)
    
    # Register blueprints (routes)
    app.register_blueprint(medicine_bp)
    app.register_blueprint(company_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Create database tables
    with app.app_context():
        db.create_all()
        print("✓ Database initialized!")
        
        # Seed initial companies if none exist
        from src.models.company import Company
        if Company.query.count() == 0:
            seed_companies()
    
    return app


def seed_companies():
    """Seed initial companies into database"""
    from src.models.company import Company
    
    initial_companies = [
        {"name": "Acme Pharma", "code": "101", "description": "Leading pharmaceutical company"},
        {"name": "HealthPlus Labs", "code": "102", "description": "Healthcare and wellness products"},
        {"name": "Pharmatech", "code": "103", "description": "Advanced pharmaceutical technology"},
        {"name": "Medicore", "code": "104", "description": "Core medical solutions"},
    ]
    
    for comp_data in initial_companies:
        company = Company(**comp_data)
        db.session.add(company)
    
    db.session.commit()
    print("✓ Seeded initial companies!")


# Create app instance
app = create_app()


if __name__ == '__main__':
    port = config.PORT
    
    print("\n" + "="*60)
    print("Pharmacy API Server")
    print("="*60)
    print(f"Server: http://localhost:{port}")
    print(f"Medicines API: http://localhost:{port}/api/medicines")
    print(f"Companies API: http://localhost:{port}/api/companies")
    print("="*60 + "\n")
    
    app.run(debug=config.DEBUG, port=port)
