#include <iostream>

int main(){

int number;
std::cout << "Enter a Number: ";
std::cin >> number;

(number % 2 != 0) ? (std::cout << "Odd Number.\n")
                  : (std::cout << "Even Number.\n");

    return 0;
}