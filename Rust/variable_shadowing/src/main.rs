fn main()
{
  /*
  Variable Shadowing means redeclaring a variable. The original variable is "replaced" by the new
  one.
  */
    let _grams_of_protein = "100.345";
    println!("{_grams_of_protein}");
    let _grams_of_protein = 100.345;
    println!("{_grams_of_protein}");
    let mut _grams_of_protein = 100;
    println!("{_grams_of_protein}");
    _grams_of_protein = _grams_of_protein * 2;
    println!("{_grams_of_protein}");
}
