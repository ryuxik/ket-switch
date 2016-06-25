"""
This is the web app to connect to the internet and controll the light switch
For now, to see it, type http://localhost:5000/ into browser
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('page.html')

# @app.route('/hello/')
# def hello(name):
# 	return render_template('page.html')

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')