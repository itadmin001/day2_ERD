CREATE TABLE Movie (
  movie_id SERIAL PRIMARY KEY,
  movie_name VARCHAR(60),
  movie_cat VARCHAR(60),
  movie_len VARCHAR(10),
  movie_rating VARCHAR(10),
  movie_rel_date DATE,
);

CREATE TABLE Customer (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(60),
  last_name VARCHAR(60),
  email VARCHAR(100),
  phone VARCHAR(20),
  preferred_contact VARCHAR(20)
);

CREATE TABLE Theater (
  theater_id SERIAL PRIMARY KEY,
  theater_no VARCHAR(60),
  movie_id INTEGER,
  movie_date DATE,
  movie_time TIME,
  FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

CREATE TABLE Ticket (
  ticket_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  ticket_no BIGINT,
  theater_id INTEGER,
  avail_tickets INTEGER,
  FOREIGN KEY (theater_id) REFERENCES Theater(theater_id),
  FOREIGN KEY (ticket_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Payment_type (
  pymt_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  card_type VARCHAR(30),
  card_no BIGINT,
  card_exp DATE,
  billing_same_as_shipping BOOLEAN,
  save_card BOOLEAN,
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Cart (
  cart_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  product_id INTEGER,
  sub_total INTEGER,
  tax INTEGER,
  FOREIGN KEY (product_id) REFERENCES Concession(product_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Concession (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(60),
  product_price INTEGER
);

CREATE TABLE Genres(
    genre_id INTEGER PRIMARY KEY,
    genre_name VARCHAR(30)
);

ALTER TABLE Movie ADD genre_id INTEGER;
ALTER TABLE Movie ADD FOREIGN KEY (genre_id) REFERENCES Genres(genre_id); 

ALTER TABLE theater DROP COLUMN movie_date;

ALTER TABLE ticket ADD COLUMN movie_time TIME;
ALTER TABLE ticket ADD COLUMN movie_date DATE;
     


