from flask import Flask
from flask import render_template
# from bs4 import BeautifulSoup
# import urllib2

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
	lis = [1,1241,4,453,-45, 45,2,23]
	return render_template("index.html", lis = sorted(lis, reverse=True))

@app.route('/cool-stuff')
@app.route('/about-me')
@app.route('/secrets')
def ohno():
	return render_template("404.html", lol = range(13))

app.run(debug = True)