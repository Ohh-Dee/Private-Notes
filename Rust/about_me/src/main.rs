/*
Hello I am here to show you how to build your own rust program with cargo commands!
First after having everything installed you will run cargo new about_me which will create
a src with your main.rs file a cargo.lock and cargo.toml file as well.
then you will set the function with the fn prefix and main(){} it should look like the following:
fn main(){}

After doing so you will put your code within the {} which most common use can be refered to macros.

the println!(); marco serves as a print line and will display what is within its ().
Do not forget to end the line with ; at the every end of your code this functions as a . in a
sentence.

you can then run a cargo check command which will run a mock of building your code to see if it has
any errors that will appear while building your exe before doing so.

Also make use of the cargo fmt command which will format your code if there is any extra space
and make your code more readable.
*/

fn main()
{
    println!("Hello, world! My name is Oscar!");
    println!("This is my first Rust build from start.");
    println!("I hope I am able to contribute alot more than this!");
}
