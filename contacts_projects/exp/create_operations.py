"""
make a python file to operation in the file 
"""

import sqlite3

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



def main():
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




	


if __name__ == '__main__':
	try:
		make_schema()
	except:
		print("table is already made")
	

	#main function
	main()

	#print the data 
	print_data()
	#search database
	#search_data("Anny")

	#clear the database
	clear_table()







'''
def create_customer(customer):
    with connection:
        cursor.execute("INSERT INTO customer VALUES (:first, :last, :age, :city, :country)", 
        {'first':customer.first_name, 'last':customer.last_name,
         'age':customer.age, 'city':customer.city, 'country':customer.country})
    

def get_customers(city):
    cursor.execute("SELECT * FROM customer WHERE city=:city", {'city':city})
    return cursor.fetchall()

def update_city(customer, city):
    with connection:
        cursor.execute("""UPDATE customer SET city=:city 
        WHERE first_name=:first AND last_name=:last""",
        {'first':customer.first_name, 'last':customer.last_name, 'city':city})

def delete_customer(customer):
    with connection:
        cursor.execute("DELETE FROM customer WHERE first_name=:first AND last_name=:last",
        {'first':customer.first_name,'last':customer.last_name})

customer_1 = Customer('john', 'doe', 30, 'perth', 'Australia')
customer_2 = Customer('sara', 'migel', 25, 'perth', 'Australia')

create_customer(customer_1)
create_customer(customer_2)

update_city(customer_1,'sydney')

delete_customer(customer_2)

print(get_customers('perth'))
print(get_customers('sydney'))

connection.close()
'''
