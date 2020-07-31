
import os

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or 'sqlite'
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name,)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"55555",
        "HOST":"118.178.180.115",
        "PORT":"3306",
        "NAME":"flask_test"
    }

    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class Testing(Config):
    Testing=True
    SQLALCHEMY_ECHO = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "55555",
        "HOST": "118.178.180.115",
        "PORT": "3306",
        "NAME": "flask_test"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "55555",
        "HOST": "118.178.180.115",
        "PORT": "3306",
        "NAME": "flask_test"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)




envs={
    "develop":DevelopConfig,
    "testing":Testing,
    "product":ProductConfig,
    "default":DevelopConfig
}