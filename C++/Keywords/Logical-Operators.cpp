#include <iostream>

int main()
{
/*
&& = check if two conditions are true (and)
|| = check if at least one of the two conditions are true (or)
! = reverses the logical state of its operand (is not)
*/

int temp;

std::cout << "Enter the Temp: ";
std::cin >> temp;

if(temp > 0 && temp < 30){

    std::cout << "The temp is Good!";

}
else{

    std::cout << "The temp is bad!";
}

    return 0;
}