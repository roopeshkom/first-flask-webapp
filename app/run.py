from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import urllib2

app = Flask(__name__)
# html = urllib2.urlopen('https://www.google.com').read()
# soup = BeautifulSoup(html, 'html.parser')


@app.route('/')
@app.route("/index")
def hello():
	lis = [1,1241,4,453,-45, 45,2,23]
	lis = sorted(lis, reverse = True)
	return render_template("index.html", lis = lis, url = "https://www.facebook.com")

app.run(debug = True)
