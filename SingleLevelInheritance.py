class Base:
	def __init__(self):
		self.i=11
		self.j=21
		print("Inside Base constructor")

	def Fun(self):
		print("Inside Base Fun")

	def Gun(self):
		print("Inside Base Gun")

#class Derived: public Base cpp
#class Derived extends Base java
class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		self.x=31
		self.y=41
		print("Inside Derived constructor")

	def Sun(self):
		print("Inside Derived Sun")

	def Gun(self):		#Overriding
		print("Inside Derived Gun")


def main():
	bObj=Base()
	print(bObj.i)
	print(bObj.j)
	bObj.Fun()
	bObj.Gun()

	dObj=Derived()
	print(dObj.i)
	print(dObj.j)
	print(dObj.x)
	print(dObj.y)
	dObj.Sun()
	dObj.Gun()
	dObj.Fun()

if __name__=="__main__":
	main()