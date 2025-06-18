from flask import Flask
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv
import os
 
load_dotenv() #load environment variables from .env
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    return app

app = create_app()
try:
    app.db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    print("Database Connection established")
except mysql.connector.Error as e:
    print("Database Connection failed")
from .routes import main as main_blueprint
app.register_blueprint(main_blueprint)