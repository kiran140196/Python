class Student:
	School="Shivaji"		#class variable

	def __init__(self,iNo1,iNo2,iNo3):
		self.m1=iNo1		#instance variable
		self.m2=iNo2
		self.m3=iNo3


	def Instance_Total(self):	#instance method
		print("Inside instance method")
		return self.m1+self.m2+self.m3

	
	@classmethod			#Decorator
	def Class_DisplaySchool(cls):	#class method
		print("School is:",cls.School)


	@staticmethod			#Decorator
	def Static_Info():		#staitc method
		print("This class contains the information of school")


def main():
	Student.Class_DisplaySchool()
	obj1=Student(80,70,50)
	obj2=Student(65,80,75)
	iRet=obj1.Instance_Total()	#calling instance method
	print("Total obtained marks",iRet)
	Student.Static_Info()
	obj1.Static_Info()		#Not good practice

if __name__=="__main__":
	main()