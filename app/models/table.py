from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    cpf = db.Column(db.String, unique=True)
    telefone = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property 
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)   

    def __init__(self, username, password, name, email, cpf, telefone):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
