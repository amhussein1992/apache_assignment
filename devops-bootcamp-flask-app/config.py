# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
#     SQLALCHEMY_DATABASE_URI = (
#         os.environ.get('DATABASE_URL')
#         or 'mysql+pymysql://root:admin@localhost:3306/devopsdb'
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


import os

class Config:
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'yourpassword')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'devopsdb')
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecret')