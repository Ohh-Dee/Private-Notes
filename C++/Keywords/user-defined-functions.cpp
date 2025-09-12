#include <iostream>


void happyBirthday(const std::string& name) {
    std::cout << "Happy Birthday to you!\n";
    std::cout << "Happy Birthday to you!\n";
    std::cout << "Happy Birthday " << name << "!\n";
    std::cout << "Happy Birthday to you!\n";
}


int main() {
    std::cout << "What is your name? ";
    std::string name;
    std::getline(std::cin >> std::ws, name);  // reads full name with spaces
    happyBirthday(name);
    return 0;
}