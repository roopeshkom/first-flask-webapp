from flask import Flask
from flask import render_template
# from bs4 import BeautifulSoup
# import urllib2

class pairs(object):
	def __init__(self):
		self.list = []

	def add(self, a, b):
		self.list.append((a, b))

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
	lis = pairs()
	lis.add(123, "apples")
	lis.add(-33, "boyo")
	lis.add(2, "ginga")

	return render_template("index.html", lis = sorted(lis.list, key=lambda x:x[1]))

@app.route('/cool-stuff')
@app.route('/about-me')
@app.route('/secrets')
def ohno():
	return render_template("404.html", lol = range(13))

app.run(debug = True)