#include <iostream>

void bakePizza();
void bakePizza(std::string topping1);
void bakePizza(std::string topping1, std::string topping2);

int main()
{
    // You can have different versions of the same function
    bakePizza("pepperoni", "onion");

    return 0;
}

void bakePizza(){
    std::cout << "Here is your pizza.\n";
}
// a functions name plus a functions parameters is known as a function signature.
void bakePizza(std::string topping1){
    std::cout << "Here is your " << topping1 << " pizza!\n";
}

void bakePizza(std::string topping1, std::string topping2){
    std::cout << "Here is your " << topping1 << " and " << topping2 << " pizza!\n";
}
