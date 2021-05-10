import os
import threading
from time import sleep

def Thread1(iNo):
	print("Thread 1 is created")
	print("PID of thread1 is:",os.getpid())
	for i in range(iNo):
		sleep(1)
		print("Thread-1",i)


def Thread2(iNo):
	print("thread 2 is created")
	print("PID of thread2 is:",os.getpid())
	for i in range(iNo):
		sleep(2)
		print("Thread-2",i)


def main():
	print("Inside main")

	print("PID of main process is:",os.getpid())

	print("PID of parent process of main is:",os.getppid())
	
	iValue=100
	t1=threading.Thread(target=Thread1,args=(iValue,))
	t2=threading.Thread(target=Thread2,args=(iValue,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("End of main process")

if __name__=="__main__":
	main()