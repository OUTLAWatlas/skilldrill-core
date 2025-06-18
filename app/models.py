from app import db
from datetime import datetime

class Skilllab(db.Model):
    __tablename__ = 'skill_labs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(50), nullable=False, default='Beginner')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcownow)

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
            'difficulty' : self.difficulty,
            'created_at' : self.created_at.isoformat()
        }