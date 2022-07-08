from flask import Flask, redirect,render_template,request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#conexion de la base de datos
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_login"

db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():   
    if request.method=='POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')





