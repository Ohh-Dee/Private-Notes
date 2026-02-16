use std::io;
const TAX_RATE: f64 = 0.07;

fn read_input() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

fn main() {
    /*
    Constant - is a name assigned to a value. a constant's value cannot change. We cannot use
    mut with constants.
    Variables that are not mutable are limited to a function scope.
    Constant can be declared at any scope. This allows them to be reused in variable scopes.

    to declare a constant you will use the macro keyword const, and it can be used at the file level
    outside of functions. Good rust practice is to name your const variables in ALL CAPS. I.E.
    TAX_RATE

    You have to provide a type it will not auto assign one such as int,str,float.
    */
    println!("The Tax rate is {:.0}.",TAX_RATE * 100.00);

    println!("How much did you spend?");
    let input = read_input();

    let amount: f64 = input.parse().expect("Please enter a valid number");
    let tax = amount * TAX_RATE;
    let total = amount + tax;
    println!("Subtotal: ${:.2}", amount);
    println!("Total: ${:.2}", total);
}
