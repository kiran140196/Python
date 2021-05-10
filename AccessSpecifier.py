#public
#protected
#private

class Base:
	def __init__(self):
		self.iNo1=11		#public member
		self._iNo2=21		#protected member
		self.__iNo3=51		#pivate member

	def fun(self):			#public method
		print(self.iNo1,self._iNo2,self.__iNo3)

	def _fun(self):			#protected method
		print(self.iNo1,self._iNo2,self.__iNo3)

	def __fun(self):		#private method
		print(self.iNo1,self._iNo2,self.__iNo3)

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		self.iNo4=101

	def gun(self):
		print("From Derived class")
		print(self.iNo1)
		print(self._iNo2)
		#print(self.__iNo3)	#Not allowed private member
		self.fun()
		self._fun()
		#self.__fun()		#Not allowed private method

class Derived2(Derived):
	def __init__(self):
		Base.__init__(self)
		Derived.__init__(self)

	def sun(self):
		print("From Derived2 class")
		print(self._iNo2)
		print("Calling Base fun from Derived2")
		self.fun()
def main():
	bObj=Base()
	print(bObj.iNo1)
	print(bObj._iNo2)
	#print(bObj.__iNo3)  		#Not allowed private member
	bObj.fun()
	bObj._fun()
	#bObj.__fun()	     		#Not allowed private method

	dObj=Derived()
	dObj.gun()

	dObj1=Derived2()
	dObj1.sun()

if __name__=="__main__":
	main()