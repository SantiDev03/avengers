from models.db import db

class Heroe (db.Model):
    __tablename__ = 'heroe'

    nombre = db.Column(db.String(50), nullable = False) 
    alias = db.Column(db.String(50), nullable = False)
    habilidades = db.Column(db.String(50), nullable = False)
    actor = db.Column(db.String(200),nullable = False)
def __init__(self,nombre,alias,habilidades,actor):
    self.nombre = nombre
    self.alias =  alias
    self.habilidades = habilidades 
    self.actor = actor
def serialize (self):
    return {
        'nombre' : self.nombre,
        'alias' : self.alias,
        'habilidades' : self.habilidades,
        'actor' : self.actor
    }