import os
class Config:
    """
    general config parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2-binary://username:password@localhost/deman'

class ProdConfig(Config):
    """
    prod config child class
    """
class DevConfig(Config):
    """
    dev config child class
    """

    Debug = True

config_options={
    'development':DevConfig,
    'production' :ProdConfig
}    

    