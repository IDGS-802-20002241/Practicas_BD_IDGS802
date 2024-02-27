from flask import Flask, request, render_template,Response
from flask_wtf.csrf import CSRFProtect
import forms 
from flask import flash
from flask import g
from config import DevelopmentConfig 
from models import db
from models import Profesores
app=Flask(__name__)


app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()


'''     
Decoradores o rutas
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



@app.route("/index",methods=["GET","POST"])
def index():
    
    prof_form=forms.UserForm2(request.form)
    if request.method == 'POST' and prof_form.validate():
        profe=Profesores(nombre=prof_form.nombre.data,
                      email=prof_form.email.data,
                      apaterno=prof_form.apaterno.data,
                      amaterno=prof_form.apaterno.data,
                      edad=int(prof_form.edad.data)
                      )
        
        #insert into values()
        db.session.add(profe)
        db.session.commit()
      
        
         
    return render_template("index.html",form=prof_form)

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    
    alumn_form=forms.UserForm(request.form)
    if request.method == 'POST' and alumn_form.validate():
        nom=alumn_form.nombre.data    
        email=alumn_form.email.data    
        apaterno=alumn_form.apaterno.data   
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom)) 
        print("email: {}".format(email)) 
        print("Apellido paterno: {}".format(apaterno)) 
    return render_template("alumnos.html", form =alumn_form )
 
@app.route("/ABC_Completo",methods=["GET","POST"])
def ABC_Completo():   
    prof_form=forms.UserForm2(request.form)
    profesores=Profesores.query.all()
    
    return render_template("ABC_Completo.html",profesor=profesores)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()

