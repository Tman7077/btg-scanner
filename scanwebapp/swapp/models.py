from flask_login import UserMixin
from swapp import cred

class User(UserMixin, cred.Model):
    id = cred.Column(cred.Integer, primary_key=True)
    username = cred.Column(cred.String(150), unique=True, nullable=False)
    password = cred.Column(cred.String(150), nullable=False)