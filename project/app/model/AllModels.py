# from project.app.db import db
# from datetime import datetime

# class User(db.Model):
#     __tablename__ = 'user'
    
#     user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)

#     # Relationships with cascade delete
#     blogs = db.relationship('Blog', back_populates='user', cascade="all, delete-orphan")
#     projects = db.relationship('Project', back_populates='user', cascade="all, delete-orphan")
#     services = db.relationship('Service', back_populates='user', cascade="all, delete-orphan")
#     comments = db.relationship('Comment', back_populates='user', cascade="all, delete-orphan")

# class Blog(db.Model):
#     __tablename__ = 'blog'
    
#     blog_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='blogs')
#     comments = db.relationship('Comment', back_populates='blog', cascade="all, delete-orphan")

# class Project(db.Model):
#     __tablename__ = 'project'
    
#     project_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     github_link = db.Column(db.String(255), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='projects')

# class Service(db.Model):
#     __tablename__ = 'service'
    
#     service_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(255), nullable=False)
#     price = db.Column(db.String(255), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='services')

# class Email(db.Model):
#     __tablename__ = 'email'
    
#     email_id = db.Column(db.Integer, primary_key=True)
#     sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
#     receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
#     subject = db.Column(db.String(255), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     sent_at = db.Column(db.DateTime, default=datetime.utcnow)
#     is_read = db.Column(db.Boolean, default=False)

#     sender = db.relationship('User', foreign_keys=[sender_id], back_populates='sent_emails')
#     receiver = db.relationship('User', foreign_keys=[receiver_id], back_populates='received_emails')

# class Comment(db.Model):
#     __tablename__ = 'comment'
    
#     comment_id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
#     blog_id = db.Column(db.Integer, db.ForeignKey('blog.blog_id', ondelete="CASCADE"), nullable=False)

#     user = db.relationship('User', back_populates='comments')
#     blog = db.relationship('Blog', back_populates='comments')
