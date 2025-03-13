import time
import random
from flask_mail import Message
from project.extensions.extensions import mail
from project.app.model.User import User
from project.utils.otp_store import otp_storage
from project.app.db import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash, check_password_hash
from project.app.schema.UserSchema import UserSchema, RequestOTPSchema
from flask import jsonify

class UserRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_user(args: dict, session: scoped_session):
        try:
            hashed_password = generate_password_hash(args['password'])

            user = User(
                username=args['username'], 
                email=args['email'], 
                password=hashed_password, 

            )
            user.role = 'user'
            session.add(user)
            session.commit()  

            return user
        except IntegrityError as e:
            session.rollback()
            raise ValueError("User with this email or username already exists.")
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_user(user_id: int, session):
        # Make sure you're calling query on session, not on user_id
        return session.query(User).filter(User.user_id == user_id).first()
    
    @staticmethod
    def get_user_by_email(email: str, session):
    # Query the user by email
        return session.query(User).filter(User.email == email).first()


    @staticmethod
    def get_all_users(session: scoped_session):
        try:
            query = session.query(User)  
            users = query.all()
            return users
        except Exception as e:
            raise e


    @staticmethod
    def request_otp_repo(user):
        session = UserRepository.get_session()
        email = user.email
        # breakpoint()
        # user = session.query(User).filter(User.email == email).first()
        
        # generate otp
        otp = str(random.randint(100000, 999999))
        expiry_time = time.time() + 300
        otp_storage[email] = {'otp' : otp, "expiry_time" : expiry_time}
        
        msg = Message("Password reset OTP",sender="abdulmuhaiminkhan123@gmail.com", recipients=[email])
        msg.body = f"Your OTP for password reset is: {otp}. It is valid for 5 minutes."
        try:
            mail.send(msg)
            # breakpoint()
            return {"message" : "OTP send successfully!"}
        except Exception as e:
            return {"message" : f"error sending mail : {str(e)}"}, 500    
    
    
    @staticmethod
    def delete_user_by_id(args, session: scoped_session):
        user_id = args.get("user_id")
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            
            if not user:
                return None
            deleted_user = UserSchema().dump(user)
            session.delete(user)
            session.commit()
            
            return deleted_user
        except Exception as e:
            session.rollback() 
            raise e

