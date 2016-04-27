from flask import Flask
from flask import render_template
# from bs4 import BeautifulSoup
# import urllib2

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def hello():
	lis = [1,1241,4,453,-45, 45,2,23]
	return render_template("index.html", lis = sorted(lis, reverse=True), url = "https://www.facebook.com")

app.run(debug = True)
