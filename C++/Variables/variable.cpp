// The Following will cover Variables in C++

#include <iostream>

int main(){
    /* There are two steps into using and creating a variable.
    Declaration and assignment. 
    Starting with declaration you need to list the datatype of what you are storing
*/

   // int x; //Declaration
    // x = 5; // Assignment where we assigned x to the value of 5 as a integer.

    // You can declare and assign on one line.
    int x = 5;
    int y = 6;
    int sum = x + y;
    int age = 30;
    /*
    ** int = Integer = Whole Numbers I.E. Age, Years, Days if you try to std::cout << 7.5 it will only print 7 and drop the rest.

    ** double = Float = Number including decimals 
    double price = 10.99;
    double gpa = 2.5;
    double temperature = 25.1;

    ** char = single character = Can only store a single character for example if I tried to output std::cout << inital with the assignment of BC it will give an error and print C and not both.
    char grade = 'A';
    char inital = 'B';
    char currency = '$';

    ** bool = boolean = true or false
    bool student = true;
    bool power = false;
    bool forSale  = true;

    ** std::string = string = object that represents a sequence of text
    std::string name = "Oscar";
    std::string food = "pizza";
    std::string day = "monday"
    */

    std::string name = "Oscar";
    std::cout << x << '\n'; // This prints the value of x.
    std::cout << y << '\n'; // This prints the value of y.
    std::cout << sum << '\n';
    std::cout << "Hello " << name << '!' << '\n';
    std::cout << "You are " << age << " years old!";
    return 0;
}