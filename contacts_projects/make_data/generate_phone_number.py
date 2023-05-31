"""
the program to generate fake phone number of 10 digits staring from 8
"""

import random


"""
generate random phone number 
"""

# importing the random module
import random


mapper = {}

def generate_phone_number():
	"""
	The function to generate random phone number 
	"""

	#the phone number 
	phone_number = "8"

	for i in range(0,9):
		phone_number += str( random.randint(0,8))

	return phone_number



if __name__ == '__main__':
	for i in range(0,10):
		
		generated_phone_number = generate_phone_number()
		
		mapper[generated_phone_number] = True
	
	#print(mapper)


a = "8213136651"




"""
make the number 
"""

lst = []

count = 0

while count < 10:

	num = random.randint(0,11)

	if num not in lst:
		lst.append(num)
		count+=1



print(lst)
