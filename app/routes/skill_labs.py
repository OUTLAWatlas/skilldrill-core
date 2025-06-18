from flask import Blueprint, request, jsonify
from app import db
from app.models import SkillLab
from datetime import datetime

skill_labs_bp = Blueprint('skill_labs',__name__, url_prefix='/api/skill-labs')

@skill_labs_bp.route('/', methods=['GET'])
def get_skill_labs():
    skill_labs = SkillLab.query.all()
    return jsonify([lab.to_dict() for lab in skill_labs])

@skill_labs_bp.route('/<int:lab_id>',methods=['GET'])
def get_skill_lab(lab_id):
    skill_lab = SkillLab.query.get_or_404(lab_id)
    return jsonify(skill_lab.to_dict())

@skill_labs_bp.route('/',methods=['POST'])
def create_skill_lab():
    data = request.get_json()
    
    if not data.get('title') or not data.get('description'):
        return jsonify({'error':'Title and description are required'}), 400

    new_lab = SkillLab(
        title=data.get('title'),
        description=data.get('description'),
        difficulty=data.get('difficulty','Beginner'),
        created_at=datetime.utcnow()
    )

    db.session.add(new_lab)
    db.session.commit()

    return jsonify(new_lab.to_dict()), 201

@skill_labs_bp.route('/<int:lab_id>', methods=['PUT'])
def update_skill_lab(lab_id):
    skill_lab = SkillLab.query.get_or_404(lab_id)
    data =request.get_json()

    skill_lab.title = data.get('title', skill_lab.title)
    skill_lab.description = data.get('description', skill_lab.description)
    skill_lab.difficulty = data.get('difficulty', skill_lab.difficulty)

    db.session.commit()

    return jsonify(skill_lab.to_dict())

@skill_labs_bp.route('/<int:lab_id>', methods=['DELETE'])
def delete_skill_lab(lab_id):
    skill_lab = SkillLab.query.get_or_404(lab_id)
    db.session.delete(skill_lab)
    db.session.commit()

    return jsonify({'status': 'success','message': 'Skill lab deleted successfully'})