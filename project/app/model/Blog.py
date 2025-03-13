# from project.app.db import db
# from datetime import datetime

# class Blog(db.Model):
#     __tablename__ = 'blog'
    
#     blog_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='blogs')
#     comments = db.relationship('Comment', back_populates='blog', cascade="all, delete-orphan")