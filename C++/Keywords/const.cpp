#include <iostream>

int main(){
/*
The const keyword specifies that a variable's value is CONSTANT 
this tells the compiler to prevent anything from modifying it.
*/

const double PI = 3.14159; // Add the const prior to the data type desgination.
double radius = 10;
double circumference = 2 * PI * radius;

std::cout << circumference << "cm" << '\n';



}