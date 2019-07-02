from flask import render_template, flash, request,redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.table import User
from app.models.forms import LoginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/login", methods=["GET","POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("login"))
        else:
            return redirect(url_for("loginalert", form=form))
    return render_template('login.html', form=form)

@app.route("/loginalert", methods=["GET","POST"])
def loginalert():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("login"))
        else:
            return render_template('loginalert.html', form=form)
    return render_template('loginalert.html', form=form)

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    try:
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
    except:
        return redirect(url_for("cadastroalert"))

@app.route("/cadastroalert", methods=["GET","POST"])
def cadastroalert():
    try:
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
            return redirect(url_for("cadastro"))
    except:
        return render_template('cadastroalert.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
