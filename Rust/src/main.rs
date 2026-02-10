/*
A rust program will typically have many functions.
Function has their own role.
No rules on how many functions it is all how you want to organize it
every rust function starts with fn which tells rust we are starting a function
then we insert the function name and every rust program must have a main function
it will look like fn main(){}.
() in fn main is the parameter which is an input to a function.
This will run first always and this is the entry point to the program.
Executing a function can be more easily referred to CALLING or INVOKING the function.
*/
fn main() {
    println!("Hello, world!");
}
// To run this on linux cli cd into the src folder then use ./main or the file you crated
// to create it use the following |rustc main.rs (or your filename)
// then in cmd run it |./main (or ./(filename))
// rust will create a "exe" type file with these instructions based on your OS not all OS.
// Once you have your exe file for your OS's it doesn't need rust to run.
// In your Terminal of choice you can cd (change directories) to your .rs file and then run
// rustfmt main.rs [or (file).rs] and it will format your code for you to keep it neat.
// the command for the whole project you can use the cargo tool
// cargo fmt will format everything (include the whitespace)

/*
At the top level you can use the cargo build and it will build your whole rust code into the
exe file. Including library crates which are external dependencies that you bring into your project.

cargo build runs in debug mode by default.
debug mode is a fast Unoptimized build and its usually used prior to release and the complier
includes additional meta data to assist with finding errors in the code which results in a larger
exe.

When we are going to publish our final product we switch over to release mode which takes longer
to complie but its opmimized for run time performance which doesn't include additional debug info
so it runs faster and smaller.

Using the cargo build it will create the debug directory under target which you can run the
exe it creates there.

to build the release version you will run the following command in your terminal
cargo build --release

if you run cargo clean it will delete your target directory and you can start a cargo build from
a clean slate.
*/
