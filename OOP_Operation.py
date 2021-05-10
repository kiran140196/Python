#Desing object oriented python application which accepts N numbers from user 
#perfrom below operations
#Display all even no
#Calculate summation of all no
#Display perfect no
#Display prime no


class Numbers:
	def __init__(self,no=10):
		self.size=no
		self.arr=[]

	def __del__(self):
		print("Delocating the memory")
		del self.arr

	def Accept(self):
		print("Please enter the elements")
		for iCnt in range(self.size):
			print("Enter element :",iCnt+1)
			self.arr.append(int(input()))

	def Display(self):
		print("Elements of list are")
		for iCnt in range(self.size):
			print(self.arr[iCnt])

	def Summation(self):
		iSum=0
		for iCnt in range(self.size):
			iSum=iSum+self.arr[iCnt]

		return iSum

	def EvenDisplay(self):
		print("Even elements form list are:")
		for iCnt in range(self.size):
			if self.arr[iCnt] % 2==0:
				print(self.arr[iCnt])

	def PerfectDisplay(self):
		iSum=0
		print("Perfect elements from list are:")
		for iCnt in range(self.size):
			for iCnt1 in range(1,int(self.arr[iCnt]/2 +1)):
				if self.arr[iCnt] % iCnt1 ==0:
					iSum=iSum+iCnt1

			if iSum==self.arr[iCnt]:
				print(self.arr[iCnt])
			iSum=0

	def PrimeDisplay(self):
		flag=False
		print("Prime elements from list are")
		for iCnt in range(self.size):
			for iCnt1 in range(2,int(self.arr[iCnt]/2 + 1)):
				if self.arr[iCnt] % iCnt1 == 0:
					flag=True
					break
			if flag == False:
				print(self.arr[iCnt])
			flag=False


def main():
	print("Enter the no of elements")
	iSize=int(input())
	obj1=Numbers(iSize)
	obj1.Accept()
	obj1.Display()
	ret=obj1.Summation()
	print("Addition of all number is:",ret)
	obj1.EvenDisplay()
	obj1.PerfectDisplay()
	obj1.PrimeDisplay()

	
if __name__=="__main__":
	main()