# from project.app.db import db
# from datetime import datetime

# class Project(db.Model):
#     __tablename__ = 'project'
    
#     project_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     github_link = db.Column(db.String(255), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='projects')