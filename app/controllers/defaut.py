from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.table import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash("Login invalido, Tente novamente.")
    return render_template('login.html', form=form)

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("senha")
        name = request.form.get("name")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        
        if username and password and name and email and cpf and telefone:
            cad = User(username, password, name, email, cpf, telefone)
            db.session.add(cad)
            db.session.commit()  
        return redirect(url_for("login"))
    else:
        return render_template('cadastro.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/teste1")
def teste1():
    r = User.query.all()
    return render_template("lista.html", r=r)