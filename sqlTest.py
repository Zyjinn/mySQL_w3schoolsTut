import mysql.connector

# My own tryhard printHeader function because i'm a tryhard
# Takes in a string
# prints the string to the console surrounded with ***'s
def printHeader(string):
    print(f'\n*** {string} ***')

# Take in some sql results and loop through them, printing all results'
# Given a mysql results object, 
# Print all results in the object
def printSQLResults(result):
    for x in result:
        print(x)

# Create connection to root user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$W@9AX^SZd",
    database="myDB"
)
# Print if valid connection
print(mydb)

# create cursor (navigator)
mycursor = mydb.cursor()

# Create a DB
# mycursor.execute("CREATE DABASE myDB")

# # Show the databases
mycursor.execute("SHOW DATABASES")
printHeader("All my databases")
for x in mycursor:
    print(x)

# # Create a table
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255)) ")

# Show all the tables in myDB
mycursor.execute("SHOW TABLES")
printHeader("All my tables")
for x in mycursor:
    print(x)

# INSERTING INTO TABLES
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" # var to store sql query
# val = [
#     ('Peter', 'Somewhere'),
#     ('Rose', 'Redville 652'),
#     ('Jake', 'Statefarm'),
#     ('Judy', 'Somewhere'),
#     ('Karen', 'Your Manager'),
#     ('Stacey', 'Your backyard')
# ]
# mycursor.executemany(sql, val) 

# # Commit the changes to the DB
# mydb.commit() 

# print(mycursor.rowcount, "records inserted.")

# SELECT IN TABLES
printHeader("Using SELECT to select all in customers table")
mycursor.execute("SELECT name, address FROM customers ORDER BY name")
myresult = mycursor.fetchall() # fetch data

# Print all results found
printSQLResults(myresult)

# SELECT USING WHERE
printHeader("Using select w/ WHERE address = Somewhere")
sql = "SELECT name, address FROM customers WHERE address = %s ORDER BY name" # USE %s TO GUARD AGAINST SQLINJECT
address = ("Somewhere",)
mycursor.execute(sql, address)
myresult = mycursor.fetchall()
printSQLResults(myresult)

# WILDCARD SELECT
printHeader("Select all in customer with 'your' in the address")
sql = "SELECT * FROM customers WHERE address LIKE '%Your%' ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
printSQLResults(myresult)

# # DELETE RECORDS
# printHeader("deleting sql records where name = Jake in customers")
# sql = "DELETE FROM customers WHERE name = %s"
# name = ("Jake",)
# mycursor.execute(sql, name)

# mydb.commit()

# print(mycursor.rowcount, "Record(s) deleted!")

# DROP TABLES
print("Dropping table customers")
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

# UPDATE a table