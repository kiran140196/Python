class Base1:
	def __init__(self):
		self.i=11
		self.j=21
		print("Inside Base1 constructor")

class Base2:
	def __init__(self):
		self.x=31
		self.y=41
		print("Inside Base2 constructor")


#class Derived: public Base cpp
#class Derived extends Base java
class Derived(Base1,Base2):		#Mutliple Inheritance
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		self.a=51
		self.b=61
		print("Inside Derived constructor")


def main():
	dObj=Derived()
	print(dObj.i)
	print(dObj.j)
	print(dObj.x)
	print(dObj.y)
	print(dObj.a)
	print(dObj.b)


if __name__=="__main__":
	main()