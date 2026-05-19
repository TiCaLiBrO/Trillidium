# Chain Assignment

## Prelude

This lesson will teach something very important in Trillia, which can be found in all Trillian code.

## Handedness

Handedness, also called handage, is the side of an expression on which certain objects are placed.

For example, in `x = y`, `x` is left-handed, while `y` is right-handed because they are on the left and right side of the `=` operator.

One **very** important thing to remember is that only the leftmost object is ever changed in any line of code.
We'll take a look at an example:

    A = B = C = D

In the code above, Trillia does the following:

- `A = B` (we put `B`'s value into `A`)
- The expression becomes `A = C = D`
- `A = C` (we put `C`'s value into `A`)
- The expression becomes `A = D`
- `A = D` (we put `D`'s value into `A`)

Notice that we continually changed the value of `A` and nothing else was changed.

`B`, `C`, and `D` were copied into `A`, but only `A` was ever reassigned.
This is how all lines of code work in Trillia, with no exceptions.

## The Task

Try it yourself

- Create a variable named `x` with the value of 5.
- Create a variable named `y` with the value of 6.
- Create a variable named `z` with the value of 7.
- Write `x = y = z`.
- Then write a separate print statement for x, y, and z on separate lines.

Then run the code.


> [!IMPORTANT]
> Invisible within Sepal.
>
>     when source_code has "x = 5";;
>     and  source_code has "y = 6";;
>     and  source_code has "z = 7";;
>     and  source_code has "x = y = z";;
>     and  x = 7
>     try sepal_execution
>     catch lesson_passed = True







