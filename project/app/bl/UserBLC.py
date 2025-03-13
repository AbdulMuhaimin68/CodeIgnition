from project.app.repository.UserRepository import UserRepository
from project.app.schema.UserSchema import UserSchema, RequestOTPSchema
from flask import jsonify
from http import HTTPStatus
from project.utils.otp_store import otp_storage
from werkzeug.security import generate_password_hash
import time

class UserBLC:

    @staticmethod
    def add_user(args: dict):
        session = UserRepository.get_session()
        try:
            users = UserRepository.add_user(args, session)
            session.commit() 
            user_schema = UserSchema()
            result = user_schema.dump(users)
            return result
        except Exception as e:
            session.rollback()
            raise e
    
    @staticmethod
    def fetch_user_by_id(args):
        id = args.get("id")  
        # breakpoint()
        session = UserRepository.get_session()
        try:
            result = UserRepository.get_user(id, session)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def get_all_users():
        session = UserRepository.get_session()
        try:
            result = UserRepository.get_all_users(session)
            return result
        except Exception as e:
            raise e


    @staticmethod
    def request_repo_blc(args: dict):
        session = UserRepository.get_session()
        email = args.get('email')

        try:
            user = UserRepository.get_user_by_email(email, session)
            if not user:
                return {"error!": "User email not found!"}

            updated_user = UserRepository.request_otp_repo(user)
            session.commit()
            return updated_user 

        except Exception as e:
            session.rollback()
            return {"error!": str(e)}
        
 
    @staticmethod
    def verify_otp(args):
        session = UserRepository.get_session()
        email = args['email']
        user = UserRepository.get_user_by_email(email, session)

        if not user:
            return {'error': 'User not found'}, 404
        if email not in otp_storage:
            return {'message': 'OTP not found or expired'}, 403
        stored_otp = otp_storage[email]
        if time.time() > stored_otp["expiry_time"]:
            del otp_storage[email]  
            return {'message': 'OTP Expire'}, 403
        if stored_otp["otp"] != args['otp']:
            return {'message': 'Invalid OTP'}, 403
        user.password = generate_password_hash(args['new_password'])
        session.commit()
        del otp_storage[email]

        return {'message': "Password updated successfully!"}, 200
            
    @staticmethod
    def deleted_user_by_id(args):
        session = UserRepository.get_session()
        try:
            res = UserRepository.delete_user_by_id(args, session)
            if res:
                return {"message": "User deleted successfully", "result": res}
            else:
                return {"message": "User with this id not found!"}
        except Exception as e:
            return {"error!": str(e)}

