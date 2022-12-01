from flask import Flask
app = Flask(__name__)
from flask_login import LoginManager
import os
login = LoginManager(app)
password = os.environ.get("password")
username = os.environ.get("username")

app.config["SECRET_KEY"]= os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username= username,
    password=password,
    hostname="mateoias1.mysql.pythonanywhere-services.com",
    databasename="mateoias1$new_connector",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False