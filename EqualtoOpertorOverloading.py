class Student:
	def __init__(self,str,a,b,c):
		self.name=str
		self.m1=a
		self.m2=b
		self.m3=c

	def __eq__(self,other):
		if self.m1==other.m2 and self.m2==other.m2 and self.m3==other.m3:
			return True
		else:
			return False

def main():
	obj1=Student("Kiran",90,90,93)
	obj2=Student("Prashant",90,90,93)

	if obj1 == obj2:
		print("Both the students are same")
	else:
		print("Both students are different")

if __name__=="__main__":
	main()