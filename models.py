from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Model -> table Etudiant
class Etudiants(db.Model):
    __tablename__ = "etudiants"

    id = db.Column(db.Integer, primary_key=True)
    sexe = db.Column(db.String(1), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, sexe, first_name, last_name, email):
        self.sexe = sexe
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        def __repr__(self):
            return f'<Etudiants {self.last_name}>'