class Base:
	def __init__(self):
		print("Base Constructor")
		self.i=10
		self.j=20

	def fun(self):
		print("Base fun")

class Derived(Base):
	def __init__(self):
		#Base.__init__(self)
		#self.__init__()	Recursive call not allowed
		super().__init__()
		self.i=30
		self.j=40
		print("Derived constructor")

	def gun(self):
		print("Derived gun")
		Base.fun(self)
		self.fun()		#fun(self)
		super().fun()		#fun(self)
		#print(i)
		print(self.i)
		#print(Base.i)
		#print(super().i)


def main():
	dObj=Derived()
	dObj.gun()

if __name__=="__main__":
	main()