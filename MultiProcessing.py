import os
import multiprocessing
from time import sleep

def Process1(iNo):
	print("Process 1 is created")
	print("PID of process1 is:",os.getpid())
	print("PID of parent process of process1 is:",os.getppid())
	for i in range(iNo):
		sleep(1)
		print("Process-1",i)


def Process2(iNo):
	print("Process 2 is created")
	print("PID of process2 is:",os.getpid())
	print("PID of parent process of process2 is:",os.getppid())
	for i in range(iNo):
		sleep(2)
		print("Process-2",i)


def main():
	print("Inside main")

	print("PID of main process is:",os.getpid())

	print("PID of parent process of main is:",os.getppid())
	
	iValue=100
	p1=multiprocessing.Process(target=Process1,args=(iValue,))
	p2=multiprocessing.Process(target=Process2,args=(iValue,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	print("End of main process")

if __name__=="__main__":
	main()