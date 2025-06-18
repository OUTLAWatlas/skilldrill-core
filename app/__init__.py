from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
 
db = SQLAlchemy()

def create_app():
	load_dotenv()
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	db.init_app(app)
	CORS(app)

	from app.routes.auth import auth_bp
	from app.routes.skill_labs import skill_labs_bp
	from app.routes.resume import resume_bp
	from app.routes.cover_letter import cover_letter_bp
	from app.routes.portfolio import portfolio_bp
	from app.routes.freelance import freelance_bp
	
	app.register_blueprint(auth_bp)
	app.register_blueprint(skill_labs_bp)
	app.register_blueprint(resume_bp)
	app.register_blueprint(cover_letter_bp)
	app.register_blueprint(portfolio_bp)
	app.register_blueprint(freelance_bp)

	return app