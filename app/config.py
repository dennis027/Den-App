import os
class Config:
    """
    general config parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2-binary://postgres:macharia123@localhost/deman'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    """
    prod config child class
    """
class DevConfig(Config):
    """
    dev config child class
    """
    DEBUG = True

config_options={
    'development':DevConfig,
    'production' :ProdConfig
}    

    