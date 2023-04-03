import os
import sqlite3
import mysql.connector
from flask_mysqldb import MySQL

from urllib import request
from flask import Flask, flash, render_template, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

from sqlalchemy import create_engine


app = Flask(__name__)


# database joined
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://studentprogresspro_user:Ubp7bK1QvDidST7YjWcsQ4SW6Pgk9Jol@dpg-cgl5ov64dad69r60cqs0-a.singapore-postgres.render.com/studentprogresspro"

# postgres://studentprogresspro_user:Ubp7bK1QvDidST7YjWcsQ4SW6Pgk9Jol@dpg-cgl5ov64dad69r60cqs0-a.singapore-postgres.render.com/studentprogresspro

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

engine = create_engine('postgresql://studentprogresspro_user:Ubp7bK1QvDidST7YjWcsQ4SW6Pgk9Jol@dpg-cgl5ov64dad69r60cqs0-a.singapore-postgres.render.com/studentprogresspro')

connection = engine.raw_connection()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route('/')
def loginpage():
    return render_template('login.html')
 
@app.route('/', methods=['POST'])
def login():
    
    email = request.form['username']
    password = request.form['password']

    c = connection.cursor()

    c.execute('SELECT * FROM public."user" WHERE email=%s AND password=%s',(email, password))
    row = c.fetchone()
    
    if row:
        c1 = connection.cursor()
        c1.execute('SELECT username, password FROM public."user" WHERE username=%s AND password=%s',(email, password))
        row1 = c1.fetchone()
        email, password = row1

        username =""
        session['username'] = username

        return redirect('/home')
    
    else:
        
        flash("Enter details are wrong! Please check again")
        
        return redirect('/')

    return render_template('login.html')

@app.route('/signup')
def signupPage():
    return render_template('SignUp.html')   


if __name__ == "__main__":
    app.run(port= 3000, debug=True)    