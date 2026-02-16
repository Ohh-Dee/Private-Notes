fn main() {
    // rust by default will make a variable immutable so if you wanted to change it later on
    // it will throw an error.
    // to make a variable mutable type mut right after let to allow it to be mutable
    // while we can now change the data we cannot change the data type I.E. an int cant go to a str
    let mut gym_reps = 10;
    println!("I would like to do at least {gym_reps} reps!");

    gym_reps = 15;
    println!("I just did {gym_reps} reps so far!");

    /*
    Rust can throw an error with a code, and you can get more information regarding this by using
    the command rustc --explain {ERROR CODE IN TERMINAL}. You can also visit the rust error code
    index on the official website for a list of error codes where you can get an explanation within
    the terminal.
    */
}
