import mysql.connector
import time

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testdb"
)

# Get the cursor
cursor = mydb.cursor()

cursor.execute("""DROP TABLE users""")

# Commit the changes to the database
mydb.commit()

# Create a table named users with the specified columns and data types
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name varchar(255) NOT NULL,
  age int(3) NOT NULL,
  student_id varchar(255) NOT NULL
)""")

# Commit the changes to the database
mydb.commit()
# Start time
start_time = time.time()

# Insert 1000 records
for i in range(100):
    id = i
    name = f"User{i}"
    age = i % 100
    student_id = f"ID{i}"
    sql = f"INSERT INTO users (id, name, age, student_id) VALUES (%s, %s, %s, %s)"
    val = (id, name, age, student_id)
    cursor.execute(sql, val)
    mydb.commit()
    data = cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

# End time
end_time = time.time()

# Print the time it took to execute
print(f"MySQL Execution time: {end_time - start_time} seconds")

# Close the database connection
mydb.close()

import sqlite3

# Connect to testdb database or create it if it does not exist
conn = sqlite3.connect("test.db")


cur = conn.cursor()
cur.execute("""DROP TABLE users""")

# Commit the changes to the database
conn.commit()

# Create a table named users with the specified columns and data types
cur.execute("""CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name varchar(255) NOT NULL,
  age int(3) NOT NULL,
  student_id varchar(255) NOT NULL
)""")

# Commit the changes to the database
conn.commit()

# Close the connection

# Start time
start_time = time.time()

# Insert 1000 records
for i in range(100):
    id = i
    name = f"User{i}"
    age = i % 100
    student_id = f"ID{i}"
    sql = f"INSERT INTO users (id, name, age, student_id) VALUES (?, ?, ?, ?)"
    val = (id, name, age, student_id)
    cur.execute(sql, val)
    conn.commit()
    data = cur.execute("SELECT * FROM users")
    rows = cur.fetchall()


# End time
end_time = time.time()
print(f"SQLite Execution time: {end_time - start_time} seconds")
conn.close()




import Database

db = Database.Database("testDB.json")
# db.create_database()
db.delete_table('users')
db.create_table('users', [{'name': 'name', 'type': 'string'}, {'name': 'age', 'type': 'integer'}, {'name': 'student_id', 'type': 'string'}])

start_time = time.time()


for i in range(100):
    name = f"User{i}"
    age = i % 100
    student_id = f"ID{i}"
    db.insert_data('users',{'name':name, 'age':age ,'student_id':student_id})
    db.get_records('users')


# End time
end_time = time.time()

# Print the time it took to execute
print(f"MyDB Execution time: {end_time - start_time} seconds")