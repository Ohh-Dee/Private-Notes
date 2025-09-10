#include <iostream>
int main(){

    char op;
    double num1;
    double num2;
    double result;

    std::cout << "********** CALCULATOR **********" << '\n';

    std::cout << "Enter your Operator: ";
    std::cin >> op;

    std::cout << "Enter your First Number: ";
    std::cin >> num1;

    std::cout << "Enter your Second Number: ";
    std::cin >> num2;

    switch(op){
        case '+':
            result = num1 + num2;
            std::cout << "Result : "<< result << '\n';
            break;
        case '-':
            result = num1 - num2;
            std::cout << "Result: " << result << '\n';
            break;

        case '*':
            result = num1 * num2;
            std::cout << "Result: " << result << '\n';
            break;
        case '/':
        result = num1 / num2;
        std::cout << "Result : " << result << '\n';
        break;

        default:
            std::cout << "That wasnt a valid operator.\n";
    }


    std::cout <<"*********************************";
    return 0;
}