from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask import Flask,jsonify
from datetime import timedelta
from project.app.db import db
from project.extensions.extensions import mail
from project.blueprint.User import bp as user_bp
from project.config import Config
# from project.blueprint.Car import bp as car_bp
# from project.blueprint.Blogs import bp as blog_bp
# from project.blueprint.Contact import bp as contact_bp
# from project.blueprint.Comment import bp as comment_bp
# from project.app.model.user import User


def create_app():
    
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:smartforum123@localhost/codeignition"
    # app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["JWT_SECRET_KEY"] = "e9f2c3d8b1a5f47c9e1d0b76c4a2e3f56789abcdef1234567890abcdefabcdef"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    app.config.from_object(Config)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'abdulmuhaiminkhan123@gmail.com'
    app.config['MAIL_PASSWORD'] = 'jeak qtai tyah gbty'  # Use the generated app password
    app.config['MAIL_DEFAULT_SENDER'] = 'abdulmuhaiminkhan123@gmail.com'  # Use the same email

    
    mail.init_app(app)
    
    
    migrate = Migrate()
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app=app, db=db) 
    # jwt = JWTManager(app)
    
    # @jwt.user_lookup_loader
    # def user_lookup(jwt_header: dict, jwt_payload: dict):
    #     email = jwt_payload.get("sub")
    #     user = User.query.filter(User.email == email).first() 
    #     return user
        
    # @jwt.additional_claims_loader
    # def add_claims(identity):
        
    #     return {"role": "admin" if identity == "admin_user" else "user"}
    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
        
    #     user = User.query.filter_by(email=identity).first()  
    #     if user:
    #         print(f"Fetching User: {user.email}, Role in DB: {user.role}")  # Debugging output
    #         return {"role": user.role}  
    #     return {}

    
    
    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code
    
    app.register_blueprint(user_bp)
    # app.register_blueprint(car_bp)
    # app.register_blueprint(blog_bp)
    # app.register_blueprint(contact_bp)
    # app.register_blueprint(comment_bp)
    with app.app_context():
        db.create_all()

    return app