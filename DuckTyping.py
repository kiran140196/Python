class C:
	def LearnAndCode(self):
		print("Learning c programming")

class Cpp:
	def LearnAndCode(self):
		print("Learning cpp programming")

class Golang:
	def LearnAndCode(self):
		print("Learning Golang programming")

class Programmer:
	def Coding(self,language):
		language.LearnAndCode()


cobj=C()
cppobj=Cpp()
gobj=Golang()


obj=Programmer()
obj.Coding(cobj)
obj.Coding(cppobj)
obj.Coding(gobj)



