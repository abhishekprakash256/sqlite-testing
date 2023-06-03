"""
make a python file to operation in the file 
"""
#imports
import sqlite3
from make_data import *



DATA_NUMBER = 40

conn = sqlite3.connect("test.db")  #to make a connection to the db

#make the cursor to tun the db commands 
c = conn.cursor()


#create a database with id and name 

def make_schema():
	"""
	The function to make the schema in the database  
	"""
	c.execute("""
	CREATE TABLE names(
		Id integer,
		name text
		)""")



def insert_data(id_value,name_value):
	"""
	The function to insert data into the database
	"""
	c.execute('INSERT INTO names (id, name) VALUES (?, ?)', (id_value, name_value))

	#to make the changes permanent
	conn.commit()


def clear_table():
	"""
	the function to clear all the data
	"""
	# Delete all data from specific tables
	c.execute('DELETE FROM names')

	#to make the changes permanent
	conn.commit()



def print_data():
	"""
	The function to print all the data
	"""
	c.execute('SELECT * FROM names')

	data = (c.fetchall())

	print(data)



def search_data(search_name):
	"""
	The function to search the database
	"""
	c.execute('SELECT * FROM names WHERE name = ?', (search_name,))

	data = c.fetchall()

	if len(data) == 0:
		print("No data found")
		exit()

	print(data)



def feed_data_():
	"""
	The main function to start the program
	"""

	#star the loop

	while True:

		# take the inputs 
		exit = input("Enter q to quit and another to continue : ")

		if exit == 'q':
			break

		id_val = int(input("Enter the id value : "))

		name_val = input("Enter the name value: ")

		insert_data(id_val,name_val)



def main():
	"""
	The main function to insert the data into the sql database
	"""

	count = 0
	
	while count < DATA_NUMBER:

		#insert the data
		insert_data(data_lst[count][0],data_lst[count][1])

		count+=1





if __name__ == '__main__':
	try:
		make_schema()
	except:
		print("table is already made")
	

	#make the data 
	make_test_data(DATA_NUMBER)

	#main function
	main()

	#print the data 
	print_data()
	#search database
	#search_data("Anny")

	#clear the database
	clear_table()