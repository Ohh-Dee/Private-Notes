fn main() {
    /*
    Scope is the boundary or region of code where a name is valid or capable of being used.
    Blocks is the area between an opening of curly braces and a closing curly brace.
    */
    let _coffee_price = 5.99;
    // so for coffee_price its scope ends within the main function.
    {
        // this is a nested scope which it can see _coffee_price because it is on the outside
        // or parent scope but still within the fn main block function.
        println!("Your Coffee will cost ${_coffee_price}.");
        //once we reach the end of this nested scope any variable within this scope cannot be used
        // as it ends in this inner scope.
    }
    // if you were to create another variable with the same name within a nested scope it will
    // treat it as a unique variable and will use it first but the parent scope will still exist.
}
