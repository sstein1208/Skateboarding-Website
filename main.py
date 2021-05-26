from flask import Flask, session
from flask import render_template, request

import sqlite3
# ------------------------------------------------DB

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute('''Create Table IF NOT EXISTS spot(
  spot_name varchar,
  spot_address varchar, 
  spot_description varchar,
  borough char,
  primary key(spot_name))''')

c.execute('''Create Table IF NOT EXISTS park(
  park_name varchar,
  park_address varchar, 
  park_description varchar,
  borough char,
  primary key(park_name))''')

c.execute('''Create Table IF NOT EXISTS shop(
  shop_name varchar,
  shop_address varchar, 
  shop_description varchar,
  borough char,
  PRIMARY KEY(shop_name, borough))''')

#Manhattan Parks
c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",("Pier 62 Skatepark", "143 11th Ave, New York, NY 10011", "Description Coming Soon", 'Manhattan'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Tribeca Skatepark', '100 N Moore St, New York, NY 10013', 'Description Coming Soon', 'Manhattan'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('LES Coleman Skatepark', '62 Monroe St &, Pike St, New York, NY 10002', 'Description Coming Soon', 'Manhattan'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Riverside Skatepark', 'Riverside Dr &, W 108th St, New York, 10025', 'Description Coming Soon', 'Manhattan'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Thomas Jefferson Skatepark', 'East 114th Street and the FDR Drive Thomas Jefferson Park, New York, NY 10029', 'Description Coming Soon', 'Manhattan'))
conn.commit()

#Brooklyn Parks
c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Substance Skatepark', '314 Scholes St, Brooklyn, NY 11206', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Vans Space 198', '198 Randolph Street, Brooklyn 11237', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('McCarren Spake Park', 'Bayard Street at Lorimer Street, Brooklyn 11222', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Canarsie Spake Park', '1–199 Seaview Ave, Brooklyn, NY  11236', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",('Thomas Greene Park', 'Degraw Street at 3rd Avenue, Brooklyn 11217', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",("Owl's Head", '102 Wakeman Pl, Brooklyn 11220', 'Description Coming Soon', 'Brooklyn'))
conn.commit()

c.execute("INSERT or REPLACE INTO park VALUES(?,?,?,?)",("Homage TF", '615 Degraw Street, Brooklyn 11217','Description Coming Soon', 'Brooklyn'))
conn.commit()

#-----------------------------------
# Manhattan Shops
c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Labor Skateshop", "46 Canal St, New York, NY 10002", "Description Coming Soon", "Manhattan"))
conn.commit()

c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Uncle Funkys Boards", "128 Charles St # Store, New York, NY 10014", "Description Coming Soon", "Manhattan"))
conn.commit()

c.execute("INSERT or REPLACE INTO shop VALUES (?,?,?,?)",("Supreme", "190 Bowery, New York, NY 10012", "Description Coming Soon", "Manhattan"))
conn.commit()
# Brooklyn Shops
c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Aegir Boardworks", "99 Water St, Brooklyn, NY 11201", "Description Coming Soon", "Brooklyn"))
conn.commit()

c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Homage Skate Shop", "615 Degraw St, Brooklyn, NY 11217", "Description Coming Soon", "Brooklyn"))
conn.commit()

c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("KCDC Skateshop", "80 N 3rd St, Brooklyn, NY 11249", "Description Coming Soon", "Brooklyn"))
conn.commit()
#Queens 
c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("GrindTime Skate Shop", "90-20 Rockaway Beach Blvd, Queens, NY 11693", "Description Coming Soon", "Queens"))
conn.commit()

c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Belief NYC", "2401 29th St, Astoria, NY 11102", "Description Coming Soon", "Queens"))
conn.commit()

# Staten Island
c.execute("INSERT or REPLACE INTO shop VALUES(?,?,?,?)",("Richmond Hood Company", "827 Castleton Ave, Staten Island, NY 10310", "Description Coming Soon", "Staten Island"))

conn.commit()
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
  m_empty_msg=""
  b_empty_msg=""
  q_empty_msg=""
  bx_empty_msg=""
  si_empty_msg=""
  m_park_info=""
  b_park_info=""
  q_park_info=""
  bx_park_info=""
  si_park_info=""
  if(request.method == "GET"):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM park  WHERE Borough=?ORDER BY park_name ASC",("Manhattan",))
    m_park_info = c.fetchall()
    if len(m_park_info) == 0:
      m_empty_msg="No parks at the moment"
    
    c.execute("SELECT * FROM park WHERE Borough=? ORDER BY park_name ASC",("Brooklyn",))
    b_park_info = c.fetchall()
    if len(b_park_info) == 0:
      b_empty_msg="No parks at the moment"  

    c.execute("SELECT * FROM park WHERE Borough=? ORDER BY park_name ASC",("Queens",))
    q_park_info = c.fetchall()
    if len(q_park_info) == 0:
      q_empty_msg="No parks at the moment"  

    c.execute("SELECT * FROM park WHERE Borough=? ORDER BY park_name ASC",("Bronx",))
    bx_park_info = c.fetchall()
    if len(bx_park_info) == 0:
      bx_empty_msg="No parks at the moment"  

  
    c.execute("SELECT * FROM park WHERE Borough=? ORDER BY park_name ASC",("Staten Island",))
    si_park_info = c.fetchall()
    if len(si_park_info)==0:
      si_empty_msg="No parks at the moment"     

    return render_template("skate_parks.html",m_table=m_park_info, b_table=b_park_info, q_table=q_park_info, bx_table=bx_park_info,
    si_table=si_park_info, m_empty_msg=m_empty_msg, b_empty_msg=b_empty_msg, q_empty_msg=q_empty_msg, bx_empty_msg=bx_empty_msg, si_empty_msg=si_empty_msg)
    conn.close()
 

#----------------------------------------Skate Shops
@app.route("/skate_shops", methods=["GET", "POST"])
def skate_shops():
    m_empty_msg=""
    b_empty_msg=""
    q_empty_msg=""
    bx_empty_msg=""
    si_empty_msg=""
    m_shop_info=""
    b_shop_info=""
    q_shop_info=""
    bx_shop_info=""
    si_shop_info=""
    if(request.method == "GET"):
      conn = sqlite3.connect("database.db")
      c = conn.cursor()

      c.execute("SELECT * FROM shop WHERE Borough=? ORDER BY shop_name ASC",("Manhattan",))
      m_shop_info = c.fetchall()
      if len(m_shop_info) == 0:
        m_empty_msg="No shops at the moment"
      
      c.execute("SELECT * FROM shop WHERE Borough=? ORDER BY shop_name ASC",("Brooklyn",))
      b_shop_info = c.fetchall()
      if len(b_shop_info) == 0:
        b_empty_msg="No shops at the moment"  

      c.execute("SELECT * FROM shop WHERE Borough=? ORDER BY shop_name ASC",("Queens",))
      q_shop_info = c.fetchall()
      if len(q_shop_info) == 0:
        q_empty_msg="No shops at the moment"  

      c.execute("SELECT * FROM shop WHERE Borough=? ORDER BY shop_name ASC",("Bronx",))
      bx_shop_info = c.fetchall()
      if len(bx_shop_info) == 0:
        bx_empty_msg="No shops at the moment"  
  
    
      c.execute("SELECT * FROM shop WHERE Borough=? ORDER BY shop_name ASC",("Staten Island",))
      si_shop_info = c.fetchall()
      if len(si_shop_info)==0:
        si_empty_msg="No shops at the moment"     

      return render_template("skate_shops.html", m_table=m_shop_info, b_table=b_shop_info, q_table=q_shop_info, bx_table=bx_shop_info,
      si_table=si_shop_info, m_empty_msg=m_empty_msg, b_empty_msg=b_empty_msg, q_empty_msg=q_empty_msg, bx_empty_msg=bx_empty_msg, si_empty_msg=si_empty_msg)
      conn.close()
   

 # Run the Flask app
app.run(host='0.0.0.0', debug=True, port=8080)
