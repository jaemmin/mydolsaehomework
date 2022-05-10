
#include <iostream>
using namespace std;
int two_unit(int n);

int main()
{
    int input = 0;
    cout << "자연수 N의 값은?";
    cin >> input;
    cout << input;
    cout << "은 ";
    cout << two_unit(input);
    cout << "자리 이진수입니다.";
}

int two_unit(int n)
{
    int checker = 1;
    int double_checker = 2;
    while (1)
    {
        if (n > double_checker)
        {
            checker++;
            double_checker *= 2;
        }
        else
        {
            break;
        }
    }
    return checker;
}