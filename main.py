from flask import Flask, session
from flask import render_template, request
import os
# import mysql.connector
import sqlite3
conn = sqlite3.connect('schema.', check_same_thread=False)

# Create a flask app
app = Flask('app')

#home page
@app.route("/", methods=["GET", "POST"])
#----------------------------------------Home Page
@app.route("/home_page", methods=["GET", "POST"])
def home_page():
    return render_template("home_page.html")


#----------------------------------------Skate Spots
@app.route("/skate_spots", methods=["GET", "POST"])
def skate_spots():
    return render_template("skate_spots.html")


#----------------------------------------Skate Parks
@app.route("/skate_parks", methods=["GET", "POST"])
def skatep_parks():
    return render_template("skate_parks.html")

#----------------------------------------Skate Shops
@app.route("/skate_shops", methods=["GET", "POST"])
def skate_shops():
    if(request.method == "GET"):
      c = conn.cursor()
      c.execute("SELECT * FROM shop")
      shop_info = c.fetchall()
      return render_template("skate_shops.html")
   

 # Run the Flask app
app.run(host='0.0.0.0', debug=True, port=8080)
