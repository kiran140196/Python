class Base:
	def __init__(self):
		self.i=11
		self.j=21
		print("Inside Base constructor")



#class Derived: public Base cpp
#class Derived extends Base java
class Derived1(Base):
	def __init__(self):
		Base.__init__(self)
		self.x=31
		self.y=41
		print("Inside Derived1 constructor")


class Derived2(Derived1):
	def __init__(self):
		Derived1.__init__(self)
		self.a=51
		self.b=61
		print("Inside Derived2 constructor")


def main():
	dObj=Derived2()
	print(dObj.i)
	print(dObj.j)
	print(dObj.x)
	print(dObj.y)
	print(dObj.a)
	print(dObj.b)


if __name__=="__main__":
	main()