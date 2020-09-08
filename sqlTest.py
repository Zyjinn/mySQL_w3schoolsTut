import mysql.connector

# Create connection to root user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$W@9AX^SZd"
)
# Print if valid connection
print(mydb)

# create cursor (navigator)
mycusor = mydb.cursor()
