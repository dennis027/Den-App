class Config:
    """
    general config parent class
    """

class ProdConfig(Config):
    """
    prod config child class
    """
class DevConfig(Config):
    """
    dev config child class
    """

    Debug = True