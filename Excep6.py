class AgeInValid(Exception):
	def __int__(self,data):
		self.data=data

def main():
	try:
		age=int(input("Enter your age for PAN card"))
		if age < 18 :
			raise AgeInValid("Your age is less than 18")

	except AgeInValid as obj:
		print(obj)

	else:
		print("You will get PAN card within 7 working days")

if __name__=="__main__":
	main()