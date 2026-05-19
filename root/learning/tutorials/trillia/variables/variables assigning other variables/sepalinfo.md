# Variables Assigning Other Variables

## Prelude

Variables can read values and store them.
A variable's value can be read by another variable and stored just like any other value.

For example, if x = 10, then you can make y = x.
Because x = 10, and y = x, y = 10 too.

## The Task

Checklist

- Create a variable named `apple_count` and set it to be equal to 5.
- On the next line, create another variable named `orange_count`, and set it to be equal to the first variable.
- On the third line, print the value of `orange_count`.

> [!TIP]
> The `_count` suffix is the proper way to say "quantity of" or "number of" something in Trillia.
> So if you are ever taking the total count of something, use `_count`.

> [!IMPORTANT]
> Invisible within SEPAL.
>
>     when lines_of_code has "apple_count = 5\norange_count = apple_count\nprint";;
>     and standard_output = "5"
>     try sepal_execution
>     catch lesson_passed = True
>
> [next lesson](https://github.com/TiCaLiBrO/Trillia/blob/main/root/learning/tutorials/trillia/variables/reassignment/sepalinfo.md)


