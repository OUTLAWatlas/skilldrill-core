from flask import Blueprint, jsonify, request
from .models import fetch_all_users, insert_user

main = Blueprint('main',__name__)

@main.route('/',methods=['GET'])
def home():
    return jsonify({"message":"Welcome to SkillDrill.ai Backend"})

@main.route('/users',methods=['GET'])
def get_users():
    users  = fetch_all_users()
    return jsonify(users)

@main.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    insert_user(name, email, password)
    return jsonify({"message":"User created successfully"}),201