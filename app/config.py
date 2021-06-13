import os
class Config:
    """
    general config parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    """
    prod config child class
    """
class DevConfig(Config):
    """
    dev config child class
    """

config_options={
    'development':DevConfig,
    'production' :ProdConfig
}    

    