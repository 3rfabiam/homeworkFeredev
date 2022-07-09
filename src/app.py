from flask import Flask, flash, redirect,render_template,request, url_for
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,logout_user,login_required 

#modelos:
from models import ModelsUsers 

#entities:
from models.entities.User import User

app = Flask(__name__)

#conexion de la base de datos
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_login"

db=MySQL(app)
login_manager_app= LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelsUsers.get_by_id(db,id)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():   
    if request.method=='POST':
        #print(request.form['email'])
        #print(request.form['password'])

        user = User(0,request.form['email'],request.form['password'])
        loged_user = ModelsUsers.login(db,user)
        if loged_user != None:
            if loged_user.password:
                login_user(loged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid Password...")
                return render_template('auth/login.html')

        else:
            flash("User not Found...")
            return render_template('auth/login.html')

        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')





