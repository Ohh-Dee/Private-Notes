#include <iostream>

int myNum = 3; 

void printNum ();


int main(){
/*
Local variables = declared inside a function or block {}
Global variables = declared outside of all functions

Best to keep global variables to a min 
more secure if you keep it within a function. 
*/
    int myNum = 1;
    printNum();
    // Putting :: before the myNum Tells the program to use the global version.
    std::cout << ::myNum << '\n' << myNum << '\n';
    return 0;
}

void printNum(){
    int myNum = 2;
    std::cout << myNum << '\n';
}