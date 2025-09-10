#include <iostream>

main(){
    bool hungry = true;

    // hungry ? std::cout << "You are Hungry" : std::cout << "You are Full.";
// Another way to write this

    std::cout << (hungry ? "You are hungry." : "You are full");
    return 0;
}