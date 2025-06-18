from flask import Blueprint, request, jsonify
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__, url_prefix='/auth')

from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable = False)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or password:
        return jsonify({'error':'Username and password are required'}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({'error':'Username already exists'}),409
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'User registered succesfully'}),201
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username = username).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({'message':'Login Successful','user_id':user.id}),200
    else:
        return jsonify({'error':'Invalid username or password'}),401