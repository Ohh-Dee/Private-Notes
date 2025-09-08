#include <iostream>

/*

Allows a value to be assigned more than once
*/
namespace first {
int x = 1;
}
namespace second{
    int x = 2;
}

int main() {
    // if you use using namespace <namespace> you dont have to reference it example below
// using namespace first;

// you can start by saying 
// using std::cout;
// this help you reduse using this again and again.
    int x = 0;
    std::cout << x << first::x;

    return 0;

}