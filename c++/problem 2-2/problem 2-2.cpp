#include <iostream>
using namespace std;
int main()
{
	int a, b, c, d, gcd;
	cout << "a의 값은?: ";
	cin >> a;
	cout << "b의 값은?: ";
	cin >> b;
	cout << "c의 값은?: ";
	cin >> c;
	int a_output = a;
	int b_output = b;
	int c_output = c;
	if (a > b)
	{
		while (b != 0)
		{
			d = a % b;
			a = b;
			b = d;
		}
		gcd = a;
	}
	else
	{
		while (a != 0)
		{
			d = b % a;
			b = a;
			a = d;
		}
		gcd = b;
	}
	if (gcd == 1)
	{
		cout << "방정식 ";
		cout << a_output;
		cout << "x+";
		cout << b_output;
		cout << "y=";
		cout << c_output;
		cout << "의 정수해는 없습니다.";
	}
	else if (c % gcd == 0)
	{
		cout << "방정식 ";
		cout << a_output;
		cout << "x+";
		cout << b_output;
		cout << "y=";
		cout << c_output;
		cout << "의 정수해는 있습니다.";
	}
	else
	{
		cout << "방정식 ";
		cout << a_output;
		cout << "x+";
		cout << b_output;
		cout << "y=";
		cout << c_output;
		cout << "의 정수해는 없습니다.";
	}

}