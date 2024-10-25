# import sqlite3

#* Connection Established with the database
# conn = sqlite3.connect('example.db')

#* Cursor Intialised
# c = conn.cursor()

#-- executing SQL commands


#* Command For Creating A Table Inside The Database
"""
c.execute("CREATE TABLE IF NOT EXISTS customers (id INT PRIMARY KEY,name TEXT,age INT)")
"""

#* Command For Inserting Data In Rows one at a time
"""
c.execute("INSERT INTO customers VALUES (3,'gaurav',25)")
print("Command Executed Successfully!")
"""

#* Command For Inserting Multiple Values into The Database
"""
many_customers = [
                (1,'Apoorav Mukherjee',20),
                (2,'Madhav Shrotriya',14),
                (3,'Gaurav Sharma',25)
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
print("Command Executed Successfully!")
"""

#* Command For Retrieving/Querying Information from the Database

"""
c.execute("SELECT * FROM customers")
#--For Selecting only One Line
c.fetchone()
#--For Selecting More than one line
c.fetchmany(3)
#--For Selecting All the Data Present in the Database
print(c.fetchall())
"""



#* Commit commands into the database
"""conn.commit()"""
#* Close Database connection
"""conn.close()"""



# DATA TYPES IN SQL
"""
! NULL
! INTEGER
! REAL
! TEXT
! BLOB  

"""