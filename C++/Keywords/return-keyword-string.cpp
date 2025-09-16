#include <iostream>

std::string contactStrings(std::string string1, std::string string2);

int main(){

    std::string firstName = "Oscar";
    std::string lastName = "D";
    std::string fullName = contactStrings(firstName, lastName);

    std::cout << "Hello " << fullName << '.';

    return 0;
}

std::string contactStrings(std::string string1, std::string string2){
    return string1 + " " + string2;
};