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
	return render_template("index.html", url = "https://www.facebook.com")

app.run(debug = True)
