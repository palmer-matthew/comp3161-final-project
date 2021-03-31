import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    # UPLOAD_FOLDER = './uploads'


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False