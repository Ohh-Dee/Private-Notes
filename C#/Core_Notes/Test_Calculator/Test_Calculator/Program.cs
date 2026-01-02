// See https://aka.ms/new-console-template for more information
// Prints out whatever is inside of the ()
Console.WriteLine("Welcome to Calculator Program!");
// Accepts User input and stores it
Console.WriteLine("Please give input: ");
string userInput = Console.ReadLine();

// the $ is similar to Pythons f formating
Console.WriteLine($"You entered: {userInput}");

Console.ReadKey();