#include <iostream>

int main()
{
/*
Ternary Operator = replacement to an if/else statement
condition ? expression1: expression 2;
*/

int grade = 75;

grade >= 60 ? std::cout << "You Pass!" : std::cout << "You Fail!"


return 0;
}