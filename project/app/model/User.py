from project.app.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default = 'user')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Relationships with cascade delete
    # blogs = db.relationship('Blog', back_populates='user', cascade="all, delete-orphan")
    # projects = db.relationship('Project', back_populates='user', cascade="all, delete-orphan")
    # services = db.relationship('Service', back_populates='user', cascade="all, delete-orphan")
    # comments = db.relationship('Comment', back_populates='user', cascade="all, delete-orphan")