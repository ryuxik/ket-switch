"""
This is the web app to connect to the internet and controll the light switch
For now, to see it, type http://localhost:5000/ into browser
"""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/home')
def index():
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
need to learn angular so that if user not logged in it redirects to this :3
"""
@app.route('/', methods=['GET', 'POST'])
def login():
    error = redirect(url_for('Stranger'))
    if request.method == 'POST':
        if request.form['username'] == 'Derp' and request.form['password'] == 'Derp':
        	return redirect(url_for('index'))
        elif request.form['username'] == 'Smol' and request.form['password'] == 'Smol':
        	return redirect(url_for('index'))
        else:
            return error
    return render_template('login.html')



if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')
