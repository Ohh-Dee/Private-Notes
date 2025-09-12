#include <iostream>

int main(){

    /*
        loop(){
            loop(){
        
        
        
             }
        }
    */

int rows;
int columns;
char symbol;

std::cout <<  "How many rows?: ";
std::cin >> rows;

std::cout <<  "How many colums?: ";
std::cin >> columns;

std::cout <<  "Enter a symbol to use?: ";
std::cin >> symbol;



    for(int i = 1; i <= 3; i++){
        for(int j = 1; j <= 10; j++){
            std::cout << symbol << ' ';
        }
        std::cout << '\n';
    }
return 0;
}