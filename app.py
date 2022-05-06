from os import abort
from flask import Flask, render_template, request, redirect, flash
from models import db, Etudiants

app = Flask(__name__)

# Configuration de notre bd
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1998fabrice@localhost:5432/app_crud_flask"
db.init_app(app)

# Insertion de notre model à la bd
@app.before_first_request
def create_all():
    db.create_all()

# Interface de crétion
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    
    # insertion dans la table
    if request.method == 'POST':
        sexe = request.form['sexe']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        etudiants = Etudiants(
            sexe=sexe,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        db.session.add(etudiants)
        db.session.commit()
        flash('ok', 'success')
        return redirect('/')


# Liste des étudiant
@app.route('/', methods=['GET'])
def all_student():
    # Affiche tout les etudiants
    students = Etudiants.query.all()
    return render_template('index.html', students=students)

# Modifier
@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    # Modifier les informations
    student = Etudiants.query.filter_by(id=id).first()

    # insertion dans la table
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        sexe = request.form['sexe']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        student = Etudiants(
            sexe=sexe,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    #return f"L'étudiant avec l'id = {id} n'existe pas !"

    return render_template('update.html', student=student)

# Supprimer
@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    # Requete pour supprimer
    student =  Etudiants.query.filter_by(id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')


if __name__ == "__main__":
    app.run(debug=True)