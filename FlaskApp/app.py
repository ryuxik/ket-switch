"""
This is the web app to connect to the internet and controll the light switch
For now, to see it, type http://localhost:5000/ into browser
"""

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('page.html')

@app.route('/376')
def Annie():
	return 'ʕ•ᴥ•ʔ'

@app.route('/673')
def Smol():
	return 'Smol'

@app.route('/Stranger')
def Stranger():
	return 'Hello stranger'

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



if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
