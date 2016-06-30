"""
This is the web app to connect to the internet and controll the light switch
For now, to see it, type http://localhost:5000/ into browser
"""
# have to pip install both flask and Flask-HTTPAuth

from flask import Flask, render_template, redirect, url_for, request, g
from functools import wraps
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)

app = Flask(__name__)

"""other login stuff"""
class Anonymous(AnonymousUserMixin):
	name = u"Anonymous"

class User(UserMixin):
	def __init__(self, name, id, active = True):
		self.name = name
		self.id = id
		self.active = active

	def is_active(self):
		#code to check if user is active goes here
		return self.active

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

USERS = {
	1: User(u"Derp", 1),
	2: User(u"Smol", 2),
	3: User(u"Stranger", 3, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.values())

SECRET_KEY = "huhh"
DEBUG = True


app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(id):
	#get necesassary info from db to make a user object and return it
	return USERS.get(int(id))
"""huehue"""

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/home')
def home():
	return render_template('page.html')

@app.route('/Annie')
def Annie():
	return render_template('annie.html')

@app.route('/Santiago')
def Smol():
	return render_template('santiago.html')

@app.route('/Stranger')
def Stranger():
	return render_template('stranger.html')

"""
This is the skeleton for the things, putting your name is kinda like a login
to access use http://localhost:5000/name/ (whichever you want here)
"""
@app.route('/name/<name>')
def hello_user(name):
	if name == 'Annie':
		return redirect(url_for('Annie'))
	if name == 'Santiago':
		return redirect(url_for('Smol'))
	else:
		return redirect(url_for('Stranger'))

"""
trial login stuff
I'm trying to use a dictionary for now as a database of users 
"""



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST" and "username" in request.form:
    	username = request.form["username"]
    	if username in USER_NAMES:
    		remember = request.form.get("remember","no") == "yes"
    		if login_user(USER_NAMES[username], remember=remember):
    			return redirect(url_for("home"))
    		else:
    			return redirect(url_for('Stranger'))
    return render_template("login.html")

#need to add reauth.html
@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
	if request.method == "POST":
		confirm_login()
		return redirect(url_for("home"))
	return render_template("reauth.html")  

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('Stranger'))  		


def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if u"Anonymous":
			return redirect(url_for('login', next = request.url))
		return f(*args, **kwargs)
	return decorated_function

@app.route('/testing_page')
@login_required
def testing_page():
	return ("hey i know you..")

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
