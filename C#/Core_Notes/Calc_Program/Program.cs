// See https://aka.ms/new-console-template for more information

Console.WriteLine("Please enter a whole number: ");

int myNumber = int.Parse(Console.ReadLine()!);
Console.WriteLine("Enter another whole number: ");
int myNumber2 = int.Parse(Console.ReadLine()!);


int sumNumber = myNumber + myNumber2;

Console.WriteLine($"The sum of the numbers is {sumNumber}");

Console.ReadKey(); 