#include <iostream>
using namespace std;
int main()
{
    // For loop
    cout << "For loop:" << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << i << " ";
    }
    cout << endl;

    // While loop
    cout << "While loop:" << endl;
    int j = 0;
    while (j < 5)
    {
        cout << j << " ";
        j++;
    }
    cout << endl;

    // Do-while loop
    cout << "Do-while loop:" << endl;
    int k = 0;
    do
    {
        cout << k << " ";
        k++;
    } while (k < 5);
    cout << endl;


    //dimand pattern 

    cout<<"Diamond pattern: "<<endl;
    int n = 4; // Number of rows for the upper half of the diamond
    // Upper half of the diamond
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i; j++)
        {
            cout << " ";
        }
        for (int j = 1; j < 2 * i ; j++)
        {
            cout << "*";
        }
        
        cout << endl;
    }
    // Lower half of the diamond
    for (int i = n - 1; i >= 1; i--)
    {
        for (int j = 1; j <= n - i; j++)
        {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}

