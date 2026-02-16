fn main() {
    /*
     By default, variables in rust are immutable or incapable of change.
     */
    let apples_num = 5;
    // to assign a var use let then the var name then = then the value
    let oranges = 14 + 6;
    let fruits = apples_num + oranges;
    /*
    You will want to use your variables first put in your string then input {} for dynamic input
    then after the "" put a , and then put which variable you want to show up in order. You can
    also do oranges - 5 in this section in order to take away or any operator for that matter
    to print an altered result with the parameters of your choice.
    */
    //println!(
    //    "This year my garden has {} apples and {} oranges for a total of {} fruits",
    //    apples_num, oranges, fruits
    //);
    println!("This year my garden has {apples_num} apples and {oranges} oranges and {fruits} total
    fruits"); // you can also directly put in the dynamic variable in to the {} with rust update.
}
