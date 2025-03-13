import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:smartforum123@localhost/codeignition"
    JWT_SECRET_KEY = "e9f2c3d8b1a5f47c9e1d0b76c4a2e3f56789abcdef1234567890abcdefabcdef"
    JWT_EXPIRATION_DELTA = 30
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # Use environment variables
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
