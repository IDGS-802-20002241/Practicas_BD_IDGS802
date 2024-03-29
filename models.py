from flask_sqlalchemy import SQLAlchemy
import datetime
db=SQLAlchemy()

class Profesores(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    amaterno=db.Column(db.String(50))
    email=db.Column(db.String(50))
    edad=db.Column(db.String(50))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)   
    
    
class Pizzeria2(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    tamano=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    num_pizzas=db.Column(db.String(50))
    ingredietes=db.Column(db.String(200))
    total=db.Column(db.String(50))
    fecha_orden=db.Column(db.DateTime)   