// problem 3-1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
using namespace std;
int main()
{
	int array[5];
	int output_array[5];
	cout << "1번째 요소는?:";
	cin >> array[0];
	cout << "2번째 요소는?:";
	cin >> array[1];
	cout << "3번째 요소는?:";
	cin >> array[2];
	cout << "4번째 요소는?:";
	cin >> array[3];
	cout << "5번째 요소는?:";
	cin >> array[4];
	for (int i = 0; i < 5; i++)
	{
		int j = 4 - i;
		output_array[i] = array[j];
	
	}
	cout << output_array[0];
	cout << output_array[1];
	cout << output_array[2];
	cout << output_array[3];
	cout << output_array[4];
}


