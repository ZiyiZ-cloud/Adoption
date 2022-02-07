"""adoption application."""

from sqlalchemy import null
from flask import Flask, render_template, request, redirect
from models import db, connect_db, Pet
from forms import AddPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    pet = Pet.query.all()
    return render_template('home.html', pet= pet)

@app.route('/add', methods=['GET','POST'])
def add_page():
     
     form = AddPetForm()
     
     if form.validate_on_submit():
         name = form.name.data
         specie = form.specie.data
         url = form.url.data
         age = form.age.data
         notes = form.notes.data
         
         newpet = Pet(name = name, specie = specie, url = url, age = age,notes = notes)
         db.session.add(newpet)
         db.session.commit()
         
         return redirect('/')
     else:
         return render_template('add.html',form = form)

@app.route('/<int:pet_id>')
def petinfo(pet_id):
    
    pet = Pet.query.get_or_404(pet_id)
    
    return render_template('petinfo.html',pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET','POST'])
def edit_page(pet_id):
    
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.specie = form.specie.data
        pet.url = form.url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit.html',form = form,pet=pet)
        
    
    