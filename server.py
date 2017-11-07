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



@app.route('/contact', methods= ['POST'])
def email():

"""User writes info in login email    

boxes and clicks submit, which directs here"""
	
	fname = request.form.get("fname")
	lname = request.form.get("lname")
	email = request.form.get("email")
	phone = request.form.get("phone")
	message = request.form.get("message")
	
	user = User.query.filter_by(fname=fname, lname=lname, email=email, phone=phone, message=message).first()



if user:

session["user_id"] = user.user_id

# print user.user_id

flash("Thank You, %s" % user.name)





return render_template(“contact.html", user=user)                                                                                                                                                                                                                                                  
	
	
