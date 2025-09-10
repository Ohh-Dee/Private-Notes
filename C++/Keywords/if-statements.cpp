#include <iostream>


int main(){

/*
if statements = do something if condition is true. if not then it dosnt do it.

*/

int age;

std::cout << "Enter your age: ";
std::cin >> age; 

if(age >= 18){ //  >= is a comparasion operator
    std::cout << "Welcome to the site!";

}
else if(age == 0){
    std::cout << "Yea right";
}
else if(age < 0 ){
std::cout << "You havent been born yet!";

}
else{
    std::cout << "You are not old enough to be on this website.";
}

return 0;
}