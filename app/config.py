import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    # UPLOAD_FOLDER = './uploads'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin' or ''
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'Password123' or ''


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False