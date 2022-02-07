from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

species = ['cat','dog','porcupine']

class AddPetForm(FlaskForm):
    
    name = StringField('Pet name',
                       validators = [InputRequired()])
    specie = StringField('Species',
                         validators = [InputRequired(),AnyOf(species)])
    url = StringField('URL',
                      validators = [Optional(),URL()])
    age = IntegerField('Age',
                       validators = [Optional(),NumberRange(0,30)])
    notes = StringField('Notes',
                        validators = [Optional()])
