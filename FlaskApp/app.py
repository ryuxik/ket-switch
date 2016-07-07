"""
This is the web app to connect to the internet and controll the light switch
For now, to see it, type http://localhost:5000/ into browser
"""
# have to pip install both flask and Flask-HTTPAuth
# import RPi.GPIO as GPIO
# import time
from flask import Flask, render_template, redirect, url_for, request, g
from functools import wraps
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)

app = Flask(__name__)

""" pin control sutff """
frequency = 50
neutralDc = frequency*.15
topDc = frequency * .25
botDc = frequency * .05
#set your pwm pin here pls
derpPin = 7
smolPin = 7

# def readyBoard(pin, frequency):
# 	#sets pins to be referenced by number on the r pi
# 	GPIO.setmode(GPIO.BOARD)
# 	#set pin as an output pin 
# 	GPIO.setup(pin,GPIO.OUT)
# 	#sets pin as a pwm modulated pin at a frequency
# 	chosenPin = GPIO.PWM(pin, frequency)
# 	#returns pin
# 	return chosenPin

# #sets pin to set to neutral position
# def setNeutral(pin):
# 	pin.ChangeDutyCycle(neutralDc)
# #sets pin to set to 180 position
# def set180(pin):
#     pin.start(neutralDc)
# 	pin.ChangeDutyCycle(topDc)
# #sets pin to set to 0 position
# def set0(pin):
#     pin.start(neutralDc)
# 	pin.ChangeDutyCycle(botDc)
# #stops pwm 
# def stopPin(pin):
# 	pin.stop()

"""other login stuff"""
class Anonymous(AnonymousUserMixin):
	name = u"Anonymous"

class User(UserMixin):
	def __init__(self, name, passw, id, active = True):
		self.name = name
		self.passw = passw
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
	1: User(u"Derp",u"Derp", 1),
	2: User(u"Smol",u"Smol", 2),
	3: User(u"Stranger",u"Stranger", 3, False),
}

USER_NAMES = dict((u.name, u) for u in USERS.values())
USER_PASSW = dict((u.passw, u) for u in USERS.values())

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
@login_required
def home():
	return render_template('page.html')

@app.route('/Annie')
@login_required
def Annie():
	return render_template('annie.html')

# @app.route('/lightsONderp')
# def lightsONderp():
# 	pin = readyBoard(derpPin,frequency)
# 	set180(pin)
# 	time.sleep(1)
# 	setNeutral(pin)
# 	stopPin(pin)
# 	GPIO.cleanup()
# 	return redirect(url_for('Annie'))

# @app.route('/lightsOFFderp')
# def lightsOFFderp():
# 	pin = readyBoard(derpPin,frequency)
# 	set0(pin)
# 	time.sleep(1)
# 	stopPin(pin)
# 	GPIO.cleanup()
# 	return redirect(url_for('Annie'))

# @app.route('/lightsONsmol')
# def lightsONsmol():
# 	pin = readyBoard(smolPin,frequency)
# 	set180(pin)
# 	time.sleep(1)
# 	setNeutral(pin)
# 	stopPin(pin)
# 	GPIO.cleanup()
# 	return redirect(url_for('Smol'))

# @app.route('/lightsOFFsmol')
# def lightsOFFsmol():
# 	pin = readyBoard(smolPin,frequency)
# 	set0(pin)
# 	time.sleep(1)
# 	stopPin(pin)
# 	GPIO.cleanup()
# 	return redirect(url_for('Smol'))

@app.route('/Santiago')
@login_required
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
@login_required
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
    if request.method == "POST" and "username" in request.form and "password" in request.form:
    	username = request.form["username"]
    	passw = request.form["password"]
    	if username in USER_NAMES and passw in USER_PASSW:
    		remember = request.form.get("remember","no") == "yes"
    		if login_user(USER_NAMES[username], remember=remember):
    			confirm_login()
    			return redirect(url_for("home"))
    		else:
    			return redirect(url_for('Stranger'))
    return render_template("login.html")

#need to add reauth.html
#idk if we even need this :3
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

@login_manager.unauthorized_handler
def unauthorized():
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
