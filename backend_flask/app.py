"""
Flask Pharmacy API - Clean Architecture
Main application entry point
"""
from flask import Flask, jsonify
from flask_cors import CORS
from src.config.settings import config
from src.config.database import db
from src.controllers.medicine_routes import medicine_bp


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
    
    return app


# Create app instance
app = create_app()


if __name__ == '__main__':
    port = config.PORT
    
    print("\n" + "="*60)
    print("Pharmacy API Server")
    print("="*60)
    print(f"Server: http://localhost:{port}")
    print(f"API: http://localhost:{port}/api/medicines")
    print("="*60 + "\n")
    
    app.run(debug=config.DEBUG, port=port)
