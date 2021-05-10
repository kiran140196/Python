class Student:
	def __init__(self,str,a,b,c):
		self.name=str
		self.m1=a
		self.m2=b
		self.m3=c

	def __eq__(self,other):
		return ((self.m1==other.m2) and (self.m2==other.m2) and (self.m3==other.m3))

	def __gt__(self,other):
		return ((self.m1>other.m2) and (self.m2>other.m2) and (self.m3>other.m3))


def main():
	obj1=Student("Kiran",90,90,93)
	obj2=Student("Prashant",90,90,95)

	if obj1 == obj2:
		print("Both the students are same")
	else:
		print("Both students are different")

	if obj1 > obj2:
		print("First object is greater")
	else:
		print("Second object is greater")

if __name__=="__main__":
	main()






#C++ operator overloding
class Demo
{
	public :
		int i,j;

	Demo(int x,int y)
	{
		this->i=x;
		this->j=y;
	}

	Demo operator - (Demo op2)
	{
		return Demo(this->i+op2.i,this->j,op2.j);
	}

	friend Demo operator + (Demo,Demo);
};



Demo operator + (Demo op1,Demo op2)
{
	return Demo(op1.i + op2.i,op1.j+op2.j)
}












