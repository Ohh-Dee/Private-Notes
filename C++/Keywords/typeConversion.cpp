#include <iostream>
int main () {

/*
Type Conversion = conversion a value of one data type to another
implicit = automatic
explicit = precede value with new data type (int)
*/

// Implicit

// int can only display a whole number so this would change

int correct = 8;
int questions = 10;
double score = correct/(double)questions * 100; // if you dont explicty change questions to double it will int divide and make .8 = 0
// by making double (float) division you allow decimals to be added as outcomes. 
std::cout << score << "%.";


return 0;
}