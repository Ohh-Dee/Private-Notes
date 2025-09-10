#include <iostream>

int main()
{
    char grade;
    std::cout << "What Letter Grade?: ";
    std::cin >> grade;

    switch (grade)
    {
    case 'A':
        std::cout << "You did Great!";
        break;
    case 'B':
        std::cout << "Thats pretty Good!";
        break;
    case 'C':
        std::cout << "You Passed!";
        break;
    case 'D':
        std::cout << "Better luck next time!";
        break;
    case 'F':
        std::cout << "Theres always room for improvement!";
        break;
    default:
        std::cout << "Enter a Letter Grade (A,B,C,D,F)";
    }

    return 0;
}