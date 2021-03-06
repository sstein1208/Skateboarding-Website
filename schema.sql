DROP TABLE IF EXISTS spot;
Create Table spot(
  spot_name varchar,
  spot_address varchar, 
  spot_description varchar,
  borough char,
  -- Photo BLOB,
  primary key(spot_name)
);

DROP TABLE IF EXISTS park;
Create Table park(
  park_name varchar,
  park_address varchar, 
  park_description varchar,
  borough char,
  -- Photo BLOB,
  primary key(park_name)
);

DROP TABLE IF EXISTS shop;
Create Table shop(
  shop_name varchar,
  shop_address varchar, 
  shop_description varchar,
  borough char,
  -- Photo BLOB,
  primary key(shop_name)
);

-- Inserts
INSERT INTO park VALUES('Pier 62 Skatepark', '143 11th Ave, New York, NY 10011', 'Description Coming Soon', 'Manhattan');
INSERT INTO park VALUES('Tribeca Skatepark', '100 N Moore St, New York, NY 10013', 'Description Coming Soon', 'Manhattan');
INSERT INTO park VALUES('LES Coleman Skatepark', '62 Monroe St &, Pike St, New York, NY 10002', 'Description Coming Soon', 'Manhattan');
INSERT INTO park VALUES('Riverside Skatepark', 'Riverside Dr &, W 108th St, New York, 10025', 'Description Coming Soon', 'Manhattan');
INSERT INTO park VALUES('Thomas Jefferson Skatepark', 'East 114th Street and the FDR Drive Thomas Jefferson Park, New York, NY 10029', 'Description Coming Soon', 'Manhattan');

INSERT INTO shop VALUES('Labor Skateshop', '46 Canal St, New York, NY 10002', 'Description Coming Soon', 'Manhattan');
INSERT INTO shop VALUES('Uncle Funkys Boards', '128 Charles St # Store, New York, NY 10014', 'Description Coming Soon', 'Manhattan');
INSERT INTO shop VALUES('Supreme', '190 Bowery, New York, NY 10012', 'Description Coming Soon', 'Manhattan');





