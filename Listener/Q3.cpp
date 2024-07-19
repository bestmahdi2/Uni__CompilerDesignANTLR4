	
// member initialization
#include <iostream>
using namespace std;

class Circle {
    double radius;
  public:
    Circle(double r) : radius(r) { }
    double area() {return radius*radius*3.14159265;}
};

class Cylinder {
    Circle base;
    double height;
  public:
    Cylinder(double r, double h) : base (r), height(h) {}
    double volume() {return base.area() * height;}
};

class Base
{
public:
	int b;
	void show()
	{
		cout << b << endl;
	}
};

class Derived:public Base
{
public:
	int d;
	void show()
	{
		cout << d << endl;
	}
};

class M
{
protected:
	int m;
public:
	void get_m(int a){m=a;}
};

class N
{
protected:
	int n;
public:
	void get_n(int b){n=b;}
};

class P : public M, public N
{
public:
	void display()
	{
		cout << "m = " << m << endl;
		cout << "n = " << n << endl;
		cout << "m * n = " << m*n << endl;
	}
};

int main () {
  Cylinder foo (10,20);

  cout << "foo's volume: " << foo.volume() << '\n';
  return 0;
}

int main()
{
	Base b1, *bptr;
	bptr = &b1;
	bptr->b=100;
	// bptr->d=200; Not possible(Derived class cant be accesed from base class)
	Derived *dptr,d1;
	dptr = &d1;
	dptr->b = 100;
	dptr->d = 200;
	// If we want to use same pointer to point at different classes
	// Then we can typecast it to different class
	(*Derived) bptr->d = 200; //Pointer is typecasted to the derived class

	return 0;
}