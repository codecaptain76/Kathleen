from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session as browser_session
from secrets import amm_chain, all_chain
import pprint
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/work')
def work():
	return render_template("work.html")

@app.route('/impact')
def impact():
	return render_template("impact.html")

@app.route('/approach')
def approach():
	return render_template("approach.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/send-email', methods= ['POST'])
def email():
	email = request.form.get("email")
	
