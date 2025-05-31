# C:\Users\RyL\Desktop\ProyectoAvengers\avengers\app.py
from flask import Flask
from config.config import DATABASE_CONNECTION_URI
from models.db import db # Esta es la importación correcta de la instancia 'db'

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    from models.heroes import Heroe # Esta importación está bien aquí
    # NO DEBE HABER un 'from models.db import db' duplicado aquí
    db.create_all() # Esto creará tus tablas

if __name__ == '__main__':
    app.run(debug=True)