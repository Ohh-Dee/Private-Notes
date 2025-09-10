#include <iostream>

// cout << (insertion Operator) output
// cin >> (extraction Operator) input

int main(){

std::string name;
int age;
std::cout <<"Whats your full name?: ";
// std::cin >> name; #this will take input but wont take anything after a space

std::getline(std::cin, name); // This allows you to accept spaces by putting std::cin, name in () after std::getline.


std::cout << "What is your age?: ";
std::cin >> age;
std::cout << "Hello " << name << "!" << '\n';

std::cout << "You are " << age <<" years old!";
    return 0;
}

/*
if code reads

std::count << "What is your age?: ";
std::cin >> age; there will be a whitespace and it will print your other code without input because cin has a whitespace.
to prevent this after this code modify your getline code

std::getline(std::cin >> std::ws, name)

This should get rid of any whitespace that would create errors. 


*/