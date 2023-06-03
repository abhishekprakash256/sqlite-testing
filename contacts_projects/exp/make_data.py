"""
make the dummy data for the test data set 
"""

#imports 

import names 
import random 


#make the number 
data_lst = []

def make_test_data(data_number):
	"""
	The function to make the dummy names and the data id
	"""
	
	for i in range(0,data_number):

		name = names.get_first_name()
		data_lst.append([name,i])
