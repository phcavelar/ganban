from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from core import db
from core import login
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
#end load_user

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return "<User {}>".format(self.username)
    #end __repr__
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    #end set_password
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    #end check_password
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/{hash}?d=retro&s={size}".format(
                hash=digest,
                size=size
        )
    #end avatar
#end User

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return "<Post {}>".format(self.body)
    #end __repr__
#end Posts
