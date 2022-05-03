#include <iostream>
using namespace std;
int main()
{
	int count;
	cout << " 몇층? : ";
	cin >> count;
	for (int i = 0; i < count; i++) {
		for (int j = count - 1; j > i; j--) {
			printf(" ");
		}

		for (int j = 0; j < 2 * i + 1; j++) {
			printf("*");
		}
		printf("\n");
	}




}