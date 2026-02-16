#![allow(unused_variables)]
/*
for a global directive use #! this tells the complier to apply it to all functions not just main.
*/
type Meters = i32;
// this represents an I32 type
// You can also have a directive for the whole function.
//#[allow(unused_variables)]
fn main() {
    /*
    Type alias - is an alternate name that we can assign to an existing type.
    Benefit of a type alias is that you can provide additional context of what that type represents.

    Compiler Directive - is an annotation that tells the compiler how to parse the source code that
    we add to the code. Directive is an instruction or command to the complier which is metadata
    that we add that changes how the complier thinks.

    We write the line above whatever we want to apply the directive to.

    */
    //#[allow(unused_variables)]
    let mile_race_length:Meters = 1600;
    //#[allow(unused_variables)]
    let two_mile_race_length:Meters = 3200;
}
