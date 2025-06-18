from app import db

class Skilllab(db.Model):
    __tablename__ = 'skill_labs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.text, nullable=False)
    difficulty = db.Columnn(db.string(50), nullable=False, default='Beginner')
    created_at = db.COlumn(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
            'difficulty' : self.difficulty,
            'created_at' : self.created_at.isoformat()
        }