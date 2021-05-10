class Base1:
	def __init__(self):
		print("Inside Base1 constructor")
	def Fun(self):
		print("Base1 Fun")

class Base2:
	def __init__(self):
		print("Inside Base2 constructor")
	def Fun(self):
		print("Base2 Fun")


#class Derived: public Base cpp
#class Derived extends Base java
class Derived(Base2,Base1):		#Mutliple Inheritance
	def __init__(self):
		Base2.__init__(self)
		Base1.__init__(self)
		print("Inside Derived constructor")


def main():
	dObj=Derived()
	dObj.Fun()


if __name__=="__main__":
	main()