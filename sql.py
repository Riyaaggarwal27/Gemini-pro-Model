import sqlite3

##connect to sqlite
connection=sqlite3.connect("users.db")

#create a cursor object to inswert record,table,retrive
cursor=connection.cursor()
# cursor.execute('''drop table Student''')
table_info="""


CREATE TABLE IF NOT EXISTS user_details (
  user_id INTEGER PRIMARY KEY,
  user_name VARCHAR(255),
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  gender VARCHAR(10),
  password VARCHAR(50),
  status INTEGER
);
"""
table_info2="""
CREATE TABLE IF NOT EXISTS products (
  product_id INTEGER PRIMARY KEY,
  product_name VARCHAR(255),
  price DECIMAL(10, 2),
  description TEXT
);
"""
table_info3="""
CREATE TABLE IF NOT EXISTS orders (
  order_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  product_id INTEGER,
  quantity INTEGER,
  order_date DATE,
  FOREIGN KEY (user_id) REFERENCES user_details(user_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

"""
cursor.execute(table_info)
cursor.execute(table_info2)
cursor.execute(table_info3)


cursor.execute('''INSERT INTO user_details (user_name, first_name, last_name, gender, password, status) VALUES
('rogers63', 'David', 'John', 'Female', 'e6a33eee180b07e563d74fee8c2c66b8', 1),
('mike28', 'Rogers', 'Paul', 'Male', '2e7dc6b8a1598f4f75c3eaa47958ee2f', 1),
('rivera92', 'David', 'John', 'Male', '1c3a8e03f448d211904161a6f5849b68', 1),
('ross95', 'Maria', 'Sanders', 'Male', '62f0a68a4179c5cdd997189760cbcf18', 1),
('paul85', 'Morris', 'Miller', 'Female', '61bd060b07bddfecccea56a82b850ecf', 1),
('smith34', 'Daniel', 'Michael', 'Female', '7055b3d9f5cb2829c26cd7e0e601cde5', 1),
('james84', 'Sanders', 'Paul', 'Female', 'b7f72d6eb92b45458020748c8d1a3573', 1),
('daniel53', 'Mark', 'Mike', 'Male', '299cbf7171ad1b2967408ed200b4e26c', 1),
('brooks80', 'Morgan', 'Maria', 'Female', 'aa736a35dc15934d67c0a999dccff8f6', 1),
('morgan65', 'Paul', 'Miller', 'Female', 'a28dca31f5aa5792e1cefd1dfd098569', 1);''')

# -- Insert sample data into the products table
cursor.execute('''INSERT INTO products (product_name, price, description) VALUES
('Laptop', 999.99, 'High-performance laptop with 16GB RAM and 512GB SSD'),
('Smartphone', 499.99, 'Latest smartphone with dual-camera setup and 128GB storage'),
('Headphones', 99.99, 'Wireless headphones with noise-canceling feature');''')

# -- Insert sample data into the orders table
cursor.execute('''INSERT INTO orders (user_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-02-20'),
(2, 2, 1, '2024-01-23'),
(3, 3, 4, '2024-09-11');''')


print("the inserted records are")
data=cursor.execute('''SELECT *FROM user_details''').fetchall()
data2=cursor.execute('''SELECT *FROM products''').fetchall()
data3=cursor.execute('''SELECT *FROM orders''').fetchall()
for row in data:
    print(row)
for row2 in data2:
    print(row2)
for row3 in data3:
    print(row3)

##close the connection
connection.commit()
connection.close()