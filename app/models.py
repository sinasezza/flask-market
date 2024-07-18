from flask_login import UserMixin

from . import bcrypt, db, login_manager


@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Float, nullable=False, default=1000.99)
    items = db.relationship("Item", backref="owner", lazy=True)
    
    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password: str):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    def check_password_correction(self, attempted_password: str):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.budget}')"

# =======================================================================================

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    description = db.Column(db.String(length=1024), nullable=True)
    price = db.Column(db.Float(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item('{self.name}', '{self.barcode}', '{self.description}', '{self.price}')"
