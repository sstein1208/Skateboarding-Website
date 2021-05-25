from flask import Flask, session
from flask import render_template, request

import sqlite3
# ------------------------------------------------DB

conn = sqlite3.connect("database.db")
c = conn.cursor()

CREATE_SPOTS = """Create Table spot(
  spot_name varchar,
  spot_address varchar, 
  spot_description varchar,
  borough char,
  primary key(spot_name)
);"""

CREATE_PARKS="""Create Table park(
  park_name varchar,
  park_address varchar, 
  park_description varchar,
  borough char,
  primary key(park_name)
);"""

CREATE_SHOPS="""Create Table shop(
  shop_name varchar,
  shop_address varchar, 
  shop_description varchar,
  borough char,
  PRIMARY KEY(shop_name, borough)
);"""

c.execute("""INSERT or REPLACE INTO shop VALUES("Labor Skateshop", "46 Canal St, New York, NY 10002", "Description Coming Soon", "Manhattan");""")

c.execute("""INSERT or REPLACE INTO shop VALUES("Uncle Funkys Boards", "128 Charles St # Store, New York, NY 10014", "Description Coming Soon", "Manhattan");""")

c.execute("""INSERT or REPLACE INTO shop VALUES("Supreme", "190 Bowery, New York, NY 10012", "Description Coming Soon", "Manhattan");""")

c.execute("""INSERT or REPLACE INTO shop VALUES("Aegir Boardworks", "99 Water St, Brooklyn, NY 11201", "Description Coming Soon", "Brooklyn");""")

c.execute("""INSERT or REPLACE INTO shop VALUES("Homage Skate Shop", "615 Degraw St, Brooklyn, NY 11217", "Description Coming Soon", "Brooklyn");""")

# conn.commit()
conn.close()
# ----------------------------------------------------
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
      conn = sqlite3.connect("database.db")
      c = conn.cursor()
      c.execute("SELECT * FROM shop WHERE Borough=?",("Manhattan",))
      m_shop_info = c.fetchall()

      c.execute("SELECT * FROM shop WHERE Borough=?",("Brooklyn",))
      b_shop_info = c.fetchall()
      for i in b_shop_info:
        print(i)

      c.execute("SELECT * FROM shop WHERE Borough=?",("Queens",))
      q_shop_info = c.fetchall()

      c.execute("SELECT * FROM shop WHERE Borough=?",("Bronx",))
      bx_shop_info = c.fetchall()

      c.execute("SELECT * FROM shop WHERE Borough=?",("Staten Island",))
      si_shop_info = c.fetchall()
      return render_template("skate_shops.html", m_table=m_shop_info, b_table=b_shop_info, q_table=q_shop_info, bx_table=bx_shop_info,
      si_table=si_shop_info)
      conn.close()
   

 # Run the Flask app
app.run(host='0.0.0.0', debug=True, port=8080)
