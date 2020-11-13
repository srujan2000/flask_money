from enum import unique
from flaskblog import db,login_manager
from flask_login import UserMixin

class Spec(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    date = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.String(120), nullable=False)
    wher = db.Column(db.String(60), nullable=False)
    pur = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Spec('{self.amount}', '{self.wher}', '{self.pur}')"


class Rec(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    date = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.String(120), nullable=False)
    fro = db.Column(db.String(60), nullable=False)
    reason = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Rec('{self.amount}', '{self.fro}', '{self.reason}')"

@login_manager.user_loader
def load_user(user_id):
    return Login.query.get(int(user_id))

class Login(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    email = db.Column(db.String(30),nullable = False ,unique = True)
    password = db.Column(db.String(20),nullable = False)
    
    def __repr__(self):
        return f"Login('{self.email})"
