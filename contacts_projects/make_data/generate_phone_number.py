"""
generate random phone number 
"""

# importing the random module
import random


#the numbers of phone numbers that we want to generate 
COUNT_NUMBERS = 500


class Data_Generator():
	"""
	The base class to generate the data 
	"""

	def generate_phone_number(self):
		"""
		The function to generate random phone number 
		"""

		#the phone number starts with 8
		phone_number = "8"

		for i in range(0,9):
			phone_number += str( random.randint(0,8))

		return phone_number


	def check_unique_number(self):
		"""
		The function to check the unique phone numbers
		"""
		count = 0
		phone_number_lst = []

		while count < COUNT_NUMBERS :

			generated_phone_number = self.generate_phone_number()

			if generated_phone_number not in phone_number_lst:
				phone_number_lst.append(generated_phone_number)
				count+=1

		print(phone_number_lst)




if __name__ == '__main__':
	data_gen = Data_Generator()
	data_gen.check_unique_number()
