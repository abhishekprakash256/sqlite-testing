"""
python file to make the data manipulation using the sqlite 
"""

import sqlite3

conn = sqlite3.connect("employee.db")  #to make a connection to the db

#make the cursor to tun the db commands 
c = conn.cursor()

c.execute("""
	CREATE TABLE employees(
		first text,
		last text,
		pay integer
		)""")

