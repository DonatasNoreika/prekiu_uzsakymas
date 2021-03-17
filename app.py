import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
#                                                                     'data.sqlite?check_same_thread=False')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Vartotojas(db.Model):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)

class Statusas(db.Model):
    __tablename__ = "statusas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)

class Produktas(db.Model):
    __tablename__ = "produktas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    kaina = db.Column("Kaina", db.Float)


class Uzsakymas(db.Model):
    __tablename__ = "uzsakymas"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column("Vardas", db.DateTime)
    vartotojas_id = db.Column(db.Integer, db.ForeignKey("vartotojas.id"))
    vartotojas = db.relationship("Vartotojas")


class Eilute(db.Model):
    __tablename__ = "eilute"
    id = db.Column(db.Integer, primary_key=True)
    produktas_id = db.Column(db.Integer, db.ForeignKey("produktas.id"))
    produktas = db.relationship("Produktas")
    kiekis = db.Column("Pavadinimas", db.Integer)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vartotojai")
def vartotojai():
    try:
        vartotojai = Vartotojas.query.all()
    except:
        vartotojai = []
    return render_template("vartotojai.html", vartotojai=vartotojai)

@app.route("/produktai")
def produktai():
    try:
        produktai = Produktas.query.all()
    except:
        produktai = []
    return render_template("produktai.html", produktai=produktai)


@app.route("/naujas_vartotojas", methods=["GET", "POST"])
def naujas_vartotojas():
    db.create_all()
    forma = forms.VartotojasForm()
    if forma.validate_on_submit():
        vartotojas = Vartotojas(vardas=forma.vardas.data,
                             pavarde=forma.pavarde.data)
        db.session.add(vartotojas)
        db.session.commit()
        return redirect(url_for('vartotojai'))
    return render_template("prideti_vartotoja.html", form=forma)


@app.route("/naujas_produktas", methods=["GET", "POST"])
def naujas_produktas():
    db.create_all()
    forma = forms.ProduktasForm()
    if forma.validate_on_submit():
        produktas = Produktas(pavadinimas=forma.pavadinimas.data,
                             kaina=forma.kaina.data)
        db.session.add(produktas)
        db.session.commit()
        return redirect(url_for('produktai'))
    return render_template("prideti_produkta.html", form=forma)

if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
