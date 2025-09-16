#include <iostream>

int myNum = 3; 

void printNum ();


int main(){
/*
Local variables = declared inside a function or block {}
Global variables = declared outside of all functions
*/

    printNum(myNum);
    return 0;
}

void printNum(){
    std::cout << myNum;
}