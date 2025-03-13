# from project.app.db import db
# from datetime import datetime


# class Service(db.Model):
#     __tablename__ = 'service'
    
#     service_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     price = db.Column(db.String(255), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='services')