class BaseConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "dialect+driver://username:password@host:port/database"


class DevConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tuser:123456@192.168.32.129:3306/flask_test'


class ProdConfig(BaseConfig):
    DEBUG = False
