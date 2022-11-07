# // To simplify we're going to be using the sqlite library
# // and the Python Programming language
# //
# // SQLITE3 is not automatically provided by Python.
# // You must install it!
import sqlite3

# //
# // How do databases store data?
# //
# //    Database -> Table -> Columns -> Rows
# //
# // Why use a database?
# //
# //    By using a database, you can save data even after
# //    the program is closed.
# //


# // Connect to the database
CONNECTION = sqlite3.connect('database.db')

# // Create a new TABLE
CONNECTION.execute("CREATE TABLE USERS (NAME, AGE);")




# // Insert NEW Data into the database
# //
# // If inserting a string, you must have it wrapped with ''
# //
# //    Example: 'Tristan' NOT Tristan
# //
# // If inserting a number, you don't need to wrap it with ''

# // Insert Tristan
CONNECTION.execute("INSERT INTO USERS (NAME, AGE) VALUES ('Tristan', 16)");

# // Insert Mark
CONNECTION.execute("INSERT INTO USERS (NAME, AGE) VALUES ('Mark', 24)");




# // Select data from the database
COLUMNS = CONNECTION.execute("SELECT * FROM USERS")
print(COLUMNS)

# // Access the selected rows
for ROW in COLUMNS:
   print("Name: " + ROW[0])
   print("Age: " + ROW[1])




# // Change data in the database
# // Any row in the database that has the NAME value as 'Tristan' is changed
# //
# // Therefore if there are multiple rows in the database that have the NAME
# // 'Tristan', they'll all be changed.
# // 
CONNECTION.execute("UPDATE USERS SET AGE = 17 WHERE NAME = 'Tristan'")

# // You must call CONNECTION.commit() to make the changes
CONNECTION.commit()




# // Close the connection once finished with it
CONNECTION.close()