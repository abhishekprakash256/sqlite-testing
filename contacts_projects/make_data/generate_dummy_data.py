"""
generate random phone number 
"""

# importing the random module
import random

import names


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
			phone_number += str(random.randint(0,8))

		return phone_number


	def check_unique_number(self):
		"""
		The function to check the unique phone numbers
		"""
		count = 0
		self.phone_number_lst = []

		while count < COUNT_NUMBERS :

			generated_phone_number = self.generate_phone_number()

			if generated_phone_number not in self.phone_number_lst:
				self.phone_number_lst.append(generated_phone_number)
				count+=1


	def generate_names_and_emails(self):
		"""
		The function generate the random first and last name
		"""

		self.names_lst = []
		self.email_lst = []
		count = 0
		
		while count < COUNT_NUMBERS:

			first_name = names.get_first_name()
			last_name = names.get_last_name()

			email_num =str(random.randint(0,8))
			email_num2 = str(random.randint(0,8))

			self.names_lst.append([first_name,last_name])

			self.email_lst.append(first_name.lower()+email_num+last_name.lower()+email_num2+"@gmail.com")

			count+=1





if __name__ == '__main__':
	data_gen = Data_Generator()
	data_gen.check_unique_number()
	data_gen.generate_names_and_emails()

	print(data_gen.names_lst)
	print(data_gen.phone_number_lst)
	print(data_gen.email_lst)