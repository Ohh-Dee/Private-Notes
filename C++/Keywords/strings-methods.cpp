#include <iostream>

// vist www.cplusplus.com/reference/string/string for more info

int main()
{
    std::string name;

    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    /*if(name.length() > 12){
        std::cout << "Your name cant be over 20 characters.";
    }
    else{
        std::cout << "Welcome " << name;
    }
*/
/*
    if(name.empty){
        std::cout << "You didnt enter your name."

    }
    else{
        std::cout << "Hello " << name;
    }
*/


/*
name.clear(); // This clears the input

std::cout << "Hello " << name;
*/

/*name.append("@gmail.com");
std::cout << "Your username is now " << name;
*/

// name.insert(0, "@");

// name.erase(0, 3);

std::cout << name;

    return 0;
}