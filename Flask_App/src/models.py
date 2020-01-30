from sqlalchemy.sql import func
from extensions import db

class Task(db.Model):
    
    __tablename__ = 'task'
    
    id          = db.Column(db.Integer, primary_key=True)
    task_name   = db.Column(db.String(100), nullable=False)
    created_at  = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at  = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return self.task_name