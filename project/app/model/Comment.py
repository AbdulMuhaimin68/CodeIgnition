# from project.app.db import db
# from datetime import datetime

# class Comment(db.Model):
#     __tablename__ = 'comment'
    
#     comment_id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
#     blog_id = db.Column(db.Integer, db.ForeignKey('blog.blog_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='comments')
#     blog = db.relationship('Blog', back_populates='comments')