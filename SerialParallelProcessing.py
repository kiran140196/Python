import os
import time
import multiprocessing

def Square(no):
	return no*no

def ParallelProcessing():
	start=time.time()
	print("Parallel Processing")
	arr=range(100)

	pobj=multiprocessing.Pool()
	ret=pobj.map(Square,arr)	

	for i in arr:
		ret.append(Square(i))

	end=time.time()
	print("Time required for parallel processing is:",end-start)


def SerialProcessing():
	start=time.time()
	print("Serial Processing")
	arr=range(10)
	ret=[]

	for i in arr:
		ret.append(Square(i))

	end=time.time()
	print("Time required for serial processing is:",end-start)

def main():
	print("Inside main")
	SerialProcessing()
	ParallelProcessing()

if __name__=="__main__":
	main()