from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import app

def get_pk(obj):
    return str(obj)

def vartotojas_query():
    return app.Vartotojas.query

class VartotojasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    submit = SubmitField('Įvesti')

class ProduktasForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', [DataRequired()])
    kaina = FloatField('Kaina', [DataRequired()])
    submit = SubmitField('Įvesti')

class UzsakymasForm(FlaskForm):
    vartotojas = QuerySelectField(query_factory=vartotojas_query, get_label="vardas", get_pk=get_pk)
    submit = SubmitField('Įvesti')