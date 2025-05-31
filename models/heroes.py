from models.db import db

class Heroe (db.Model):
    __tablename__ = 'heroe'

    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100), nullable=False)
    habilidad = db.Column(db.String(200), nullable=False) 
    actor = db.Column(db.String(200), nullable=False)

def __init__(self,nombre,alias,habilidades,actor):
    self.nombre = nombre
    self.alias =  alias
    self.habilidades = habilidades 
    self.actor = actor
def serialize (self):
    return {
        'id' : self.id,
        'nombre' : self.nombre,
        'alias' : self.alias,
        'habilidades' : self.habilidades,
        'actor' : self.actor
    }