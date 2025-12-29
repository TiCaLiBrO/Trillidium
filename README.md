# **Trillia**
Trillia is a general-purpose computer programming language designed to be minimal, deterministic, low-level-capable, and be maximally easy to learn, to read, and to write.
Trillia is inspired by C, Python, Go, and Lua.

The simplicity and pseudo-code-like design of Python is always easy to see in Trillia.
Many consistent design choices have been implemented from Lua.
The focus on parallelism, and the idea of convergent programming to make debugging easy, as well as the simplicity revolving around rapidity of onboarding makes Trillia resemble Go's design in many ways.
The low-level nature, and absolute simplicity of C is present in Trillia, with Trillia only having about 7 core features.
That means, if you learn a feature a day, you can learn Trillia in a week.

These seven core features are namely: Variables, Control Structures, Vectors, Symbolics, Reactives, Functions, and Threads.

Trillia has some features that are not seen in its 'parent' languages. Namely, reactivity is a major focal point of Trillia, and unlike Go and C, Trillia's parallel threading is fully deterministic.
In fact, the entire language is fully deterministic aside from certain functions or imports, such as random, time and unsafe functions.

The Implementation of Trillia is language agnostic.
It doesn't matter whether Trillia is transpiled, compiled, or interpreted, and it also doesn't matter which languages are used to implent Trillia, as long as it behaves deterministically and is true to Trillia's blueprints.
An ideal Trillia implementation would be a boostrapped Trillia that compiles to C or C++. This is because C is very fast, low-level, unrestrictive, and has many libraries and modules.
Trillia should also always have full access to functions, libraries, and keywords of the language that it compiles to to ensure maximal tooling. If it compiles to a language, it should be able to take advantage of the language that it runs on.

**An Overview of the language:**

# 1. Whitespace

Trillia is whitespace significant. Indentation replaces the need for brackets, and new line characters replace the need for semicolons. Minimalism is prioritized.
One of the goals of Trillia is to have code be written how a progammer thinks, and maximize quality of life. Your code should look like pseudo code, and you should never be fighting against the syntax.
If you wish to have multiple statements on a single line of code, or just wish to be explicit, you can optionally use `;` as an alternative to the `\n` character.
There are certain occations where `;` is reccomended for clarity, such as declaration without assignment.
If you wish to have a single statement be split across multiple lines, you can use `;;` to nullify the `\n` new line character. This ensures that you can format code in the way that you like.
Indented code is called **subordinate code**, and the code that is dedented above that subordinate code is called **ordinate code**. Indentation is 4 spaces.

Spaces are important and enforced. To ensure maximal clarity, operations are split into different categories:

* **Binary Operations** require a space before and after them. `a / b` is allowed, but not `a/ b`, `a /b` or `a/b`.

* **Suffix Unary Operations** must be attached to the end of what they modify. For example, attaching the `%` symbol to the end of a number will divide that number by 100. `10%` returns `0.1`.

* **Prefix Unary Operations** must always be prepended to what they modify. For example the `-` symbol can be prepended to a variable to flip its sign. For example: if you have a variable x = 12, then -x is -12.

# 2. Unified Assignment Operator
In Trillia, the `=` sign is used for assignments of *all* objects.

Variables, Control Structures, Vectors, Types, Reactives, Functions, and Threads are *all* given value using the `=` Assignment Operator.
There are *no* objects in Trillia that can be assigned value without the Assignment Operator. And this list of objects is *the entire list of all things that can be created in Trillia*.

## 2.1 Variable Assignment

Variables are assigned using a variable name, followed by the `=` sign, then the value you are assigning to it

    x = 10

To swap two variables, you can use `,` commas on both sides of the `=` sign

    a = 3
    b = 7
    a, b = b, a
This swaps the value of a and b.

You cannot do chained assignments.

    a = b = c
Is not allowed because it's ***bad code***. This is prevented to avoid confusion and maximize clarity.
If you wish to do multiple assignments on a single line, you must either use `,` or `;` to separate assignments.

    a = b; b = c
or

    a, b = b, c

You must either have an equal number of left-hand and right-hand elements, OR have many left-hand elements and only one right-hand element.

Having many left-hand elements and one right-hand element will place the right-hand element's value into all left-hand containers.

    a, b, c, d, e = f
Here, a, b, c, d, and e all are assigned to value of f.

## 2.2 Strict Types and Sizes

If you don't use types, the variable will automatically promote or change type readily as needed. You can use strict types and sizes to ensure that the variable does not change type or size.

    int32 x = 10

If you use a type without a size, the type of the variable will remain consistent, but size promotion and demotion will occur when necessary.

    int x = 120     # this is an 8 bit integer by default because it's the smallest size that can represent this value.
    x = 300         # It was promoted to a 16 bit integer to be able to represent this value.

If you use the `scal` type (short for scalar), you can set a size but not a type. This is the same as a `union` in C.

    scal64 x = 4800
    x = -0.3333

You can use the `scal` type without a size to explicitly state that a variable is intentionally dynamic type and size instead of being a hastily programmed prototype.

    scal x = "hello"

## 2.3 Mutability

There are four keywords that change which ways your data is allowed to be altered.

* The `const` keyword, alternatively written as `constant`, will prevent your data from being altered.

* The `stat` keyword, alternatively written as `static`, will only allow your data to be assigned or reassigned but not altered or relatively reassigned.

* The `rel` keyword, alternatively written as `relative`, will only allow your data to be relatively reassigned or altered, but not assigned.

* The `mut` keyword, alternatively written as `mutable`, will allow your data to be altered in all ways. If no keyword is given, mutability is assumed by default. This is to preserve quality of life.

## 2.4 Declarations

If you wish to claim memory before assigning it a value, you can declare without assignment. It's reccomended that you use `;` for clarity, signalling that you intentionally did not provide assignment.

    int32 x;

If you have a variable with mutability restrictions, you can use a declarative line on that variable with a new mutability rule to specify a deliberate change in mutability.

    mutable x;

If you wish to cast the type and or size of a variable into another type, you can also do so by using a declarative line.

    nat32 x;
This is only possible if the value can be perfectly preserved. Floating points can error.
It is highly recomended that you use the `rat` rational type to be able to represent values perfectly.

## 2.5 Hard Variables

By default, when you create a variable, you are creating something called a `soft` variable. A `soft` variable is any variable that lives inside register space.
These variables are not saved, and they can be rapidly modified. These are by far the most common type of variable.

Using the `hard` keyword, variables can be stored as writes to another file. Trillia files that you program in are labelled `X.tri`, where X is a placeholder for the name of your program.
If a hard variable is created, an `X.trihard` file of the same name will be created automatically to contain all hard variable data.
Hard variables are much slower to assign or alter, but they are saved variables that don't require you to use `read()` or `write()`.

All `hard` variables persist across multiple runs of a program. This is their main purpose. They are essitially just a more user-friendly and variable-consistent way of doing write() operations.

Writing to disc space is usually very slow compared to register space. It's recommended that you make `hard` variables either read-only or read-mostly.
Here, "read-mostly" just means that read operations occur more often than write operations.
The `hard` variables are made even slower to modify by having automatic safety measures in place to prevent corruption.
During any change to a `hard` variable, a three-step process begins.
First, a copy of the variable with the newly-assigned value is created.
Then, that new value is pasted over the old value of the original copy of the variable.
And finally, the new copy is freed from memory.

A special case:

If you use `hard` + `const`, you get a literal value that is treated as a variable.

    hard const rat32 PI = 3.1415
Here, the value of pi is stored in your program at compile time. It's very similar to `#define` in C.

# 3. Types
Different data types are used best for different tasks. 
Trillia has four numeric types: `nat`, `int`, `rat`, and `float`. All of these are suffixed by the number of bits used to represent them.
For example, natX is most often in the forms `nat`, `nat8`, `nat16`, `nat32`, and `nat64`.

## 3.1 Numerics

Natural numbers `nat` are what most other languages call `unsigned integer`. The `nat` type is the most basic form of numeric data type.

Integers `int` allow negative numbers to be represented.

Rational numbers `rat` are actually an array of two numbers, a divisor and denomonator, that exist as a reduced fraction in memory. The size represents the size of both elements in the array.
The rational type is preferred over floating point where precision is more valuable than speed.

Floating point numbers `float` are exactly the same as floats usually are in other languages.

Next up is the Scalar type `scal`, which is also notated in bits.

=============================================================
UNFINISHED
=============================================================

## 3.2 Unionized Types

If the `scal` type is too unbounded, you can use unionization to specify exactly which types are allowed.
Unionization is done via typing an object multiple times in a single assignment line.

    int32 nat32 x = 24
This will always choose the first listed type (int32) if possible to represent the value of x, and then any other values are checked if it's not possible. The priority goes from left to right.

## 3.3 Built-in Symbolic Types
The next types are non-numeric, and have only one size.
`char` is 8 bits, used to represent characters in strings. They use ascii.
`bool` only has two literal values, `True` or `False`.
`Undefined` is the default value of any variable that has been declared but not assigned. If a read occurs on a value that is `Undefined`, it will cause an error.
`None` is similar to `Undefined`, except it is used to explicitly return an empty value. This doesn't crash upon read.

## 3.3 Vector Types
The vector types are: vecX, arrayX, listX, and threadX.
Vectors are suffixed not by number of bits, but instead by number of *elements* that they have. For example, `array4` holds 4 elements.
Vectors exist in two flavors: `array`s and `list`s.
Using the `vec` type, Trillia will create an `array` if possible, and a `list` if not. The `vec` type is best to use in most instances.
Using the `array` type, Trillia will attempt to create an `array`, and if the elements do not conform to the rules of arrays, an error will occur.
Using the `list` type always creates a linked list.
The `thread` type is a special type of vector. More about it later in the Threads section.

Declaration is done using the `[]` symbols

    my_list = [1, 2, 3]

    array3 int32 my_array = [1, 2, 3]

In Trillia, *everything* is an `array`. Let's restate that.
In Trillia, ***everything*** is an `array`.
Variables aren't technically arrays under the hood, but you can treat them like iterables with only one element. Everything can be treated like an `array`.
You can also turn variables into true arrays very easily by using `array` functions on them

    x = 12
    (x)append(4)
    # now x = [12, 4]

Trillia doesn't support sets, tuples, dictionaries, maps, or any other type of iterable. You make them yourself, and specify their rules.
There are many built-in functions that are best used for sets, such as `union()` or `intersection()`, and guidelines on which functions to use, but no hard rules.

## 3.4 Custom Symbolic Types (Enumerations & Dictionaries)
Custom data types are defined using a name for the type, followed by the `=` sign, followed by an `array`, of which, each element is encapsulated with \` markers, similar to `"`s or `'`s for strings.

    fruits = [`apple`, `orange`, `banana`, `plum`]
The backticks are used in the same way as strings, but unlike strings, the entire word used is treated as a literal, individual characters cannot be indexed, and they take up far less memory than strings.
The individual elements do not behave like numerics, but they can be accessed by index. Ultimately, you define the rules in which each symbol is used.
For example, you cannot say `apple + apple` and expect `orange` to be the return value unless you specifically define that to be the case.

## 3.5 Dictionaries
================================= UNFINISHED ========================================



# 4. Symbols and Operations
Trillia makes use of keyboard symbols to perform common operations.

## 4.1 Symbol Spacing
Trillia is very strict about using spaces when using symbols. This ensures greater readability.
Some symbols change meaning depending on where they are placed, so clarity through spacing is both important and enforced.
For example, `+` can mean "positive" in `+10`, "addition" in `23 + 45`, and "increment" in `6+`.
There are four main symbol types:
* Prefixes
* Suffixes
* Binary Operators
* Brackets

All prefixes must be prepended to what they modify. All suffixes must be appended to what they modify. All binary operators require at least one space before and after what they modify, and brackets must be opened and closed.

## 4.2 Order of operations
In Trillia, the order of operations is always brackets first, left to right. There is no higher precedence given to multiplication over addition, or certain functions over others.

`2 + 5 * 10` returns 70. If you want it to be done in proper order, just move things around or use brackets.

`5 * 10 + 2`   returns 52

`2 + (5 * 10)` returns 52

If there are multiple disconnected brackets in a larger expression, if your version of Trillia is implemented with automatic parallel threading, it should understand that it can solve for both pairs of parentheses at the same time.

Think of an expression like this: `(1 + 2) + (3 + 4)`

In such a case, `(1 + 2) + (3 + 4)` resolves to `(3) + (7)` in a single step, because both sides were solved simultaneusly.

If there are more brackets to solve in parallel than there are cores on your computer, left-most brackets are resolved first to preserve left-to-right execution.

## 4.3 Arithmetic Operator Symbols
For Arithmetic, Trillia has seven binary operations. You do not have to import a math library to access `pow()`, `sqrt()`, or `log()`; these operations are built into the language as symbols, and are intuitive to use.

`+` Addition

`-` Subtraction


`*` Multiplication

`/` Division


`**` Exponentiation (Powers)

`//` Radication (Roots)

`\\` Logarithmatization (Logarithms)

The symbols chosen for roots and powers are the same as the symbols for multiplication and division. The symbol for logarithms is just a mirroring of the symbol for roots.
With a system like this, you don't have to remember individual symbols, you just need to remember rules.
The logic is extendable. You could imagine tetration being written as ***, and its root and log equivalent to be written as /// and \\\ respectively.
Such operations aren't supported by Trillia due to memory restraints on most computers. Even something as simple as 5 *** 10 would blow the stack on most computers.

The notation of binary operators is:
`base` then `operation` then `modicand` then `=` then `return_value`
So in the expression `1 + 2`, `1` is the `base`, `2` is the `modicand`, `+` is the `operation`, and `3` is the `return` value.
There is no need to remember dividend, subtrahend, augend, or other operation-specific words.

Addition is commutative.

    2 + 3 = 5
    3 + 2 = 5

Subtraction will return a positive value if the base is greater than the modicand, and a negative return value if the base is less than the modicand.

    8 - 7 =  1
    7 - 8 = -1

Multiplication is commutative.

    5 * 7 = 35
    7 * 5 = 35

Division always returns a rat type or a float type if the mathematical result would return a fraction that cannot be expressed as an integer.

    int a = 2
    int b = 3
    a = a / b
This expression would error because `2 / 3` gives a non-integer return value.
To avoid this, there are different types of division.

To round your division up, down, or nearest, use `/^`, `/_`, and `/~` respectively.

    int a = 2
    int b = 3
    a = a /  b     # This errors because a is an integer and a / b returns a rational.
    a = a /^ b     # a = 1
    a = a /_ b     # a = 0
    a = a /~ b     # a = 1. In the case of 0.5, it rounds up.

There are also two more forms of division, `/%` and `/@`.
The `/%` is modulo division. It divides, and returns the remainder instead of giving a fraction.

    a /% b     # This would return 1

The `/@` can be literally read as *"divides at"* or *"is divisible by"*. Instead of returning a number, it always returns `True` or `False`.

    my_variable = a /@ b
For this expression, `my_variable` would be `False`.
The `/@` operator makes the common `a % b == 0` or `a % b != 0` expressions - that are often seen in other languages - shorter, and more readable.

    if a /@ b
        pass

Exponents are non-commutative. The modicand is always the "little number" that you see in "x squared" or "x cubed".

    2 ** 3 = 8
    3 ** 2 = 9
This can be read as *"two to the power of three is eight"*.

Roots are written in the same way, where the exponent is the modicand.
This can seem slightly confusing at first because common notation puts the exponent on the left for roots, but in Trillia, the modicand is always the exponent.

    100 // 2 = 10
    25 // 2 = 5
This can be read as *"twenty five to the root of two is five"*
Also, notice that with this notation, there is much more freedom than `sqrt()` and `cbrt()` because you are not limited. You can choose any exponent that you want, not just 2 or 3.

Roots also come with variant operations: `//_`, `//^`, `//~`, `//%`, and `//@`.
The `//_`, `//^` and `//~` operators round the result down, up, and nearest respectively.

The `//%` operator returns the remainder of a root.

    10 //% 2 = 1
because `9 // 2 = 3` exactly, and `10` is 1 more than that.
Some more examples to get the hang of it:

    27 //% 2 = 2
    16 //% 2 = 0
    99 //% 2 = 8

The `//@` operator is basically like an *`is_square()`* or *`is_cube()`* function that returns `True` if the base is a power of the modicand.

    100 //@ 2 = True
    70  //@ 9 = False

Logarithms are the same as roots, except the return value and the modicand are swapped.

    100 \\ 10 = 2
    25 \\ 5 = 2

To get natural logarithms, you can use the built-in `EULER` constant as the modicand

    10 \\ EULER = 2.30258509299

The same variant operators exist for logarithms as do exist for division and roots. `\\^`, `\\_`, `\\~`, `\\%`, `\\@`.
The `\\^`, `\\_`, `\\~` operators round as expected.

    17 \\@ 12 = False
    10 \\% 3 = 1

Incrementation and Decrementation:
As a final note on arithmetical operators, the suffixes `+` and `-` are able to be used for adding or subtracting 1 from a value.

    10+ = 11
    79- = 78

You can chain these together as long as it's only `+` or only `-`.

    3++  = 5
    0--- = -3

To prevent redundancy, and to increase readability, chaining `+` with `-` directly is not allowed.

    10++--- # this gives an error, because 10++--- can be refactored into 10-.
Under the hood, chaining `+`s or `-`s in long strings is simply condensed into addition. So `5+++++` is just `5 + 5` to prevent wasted operations.

Positive and Negative:
As a prefix, `+` makes what it affects always positive. It is an absolute value unary operator.

    +12
    g = -50
    h = +g # variable h is now 50.

As a prefix, the `-` sign always flips the sign from positive to negative, or negative to positive.

    g = -50
    h = -g # variable h is now 50.

For literals, you can only have a single `+` or `-` sign as a prefix. `--4` is not allowed because it can be reduced to `4`, or `+4` for clarity.
For variables, no sign, `+`, `-`, and `+-` are all allowed.

  g  = -50

  g is -50

 -g is  50

 +g is  50
 
+-g is -50

  i  =  20
  
  i is  20
  
 -i is -20

 +i is  20

+-i is -20

For variables, no sign before them means that you're just taking the value of the variable.
A `+` sign means you're taking the absolute value of the variable. This ensures you will get positive value.
A `-` sign means you're flipping the sign of the value of the variable. This ensures you will always get the opposite signage of the variable.
The `+-` means you're doing `+`, which makes the value of the variable positive, and then `-`, which flips the sign. This ensures you will always get negative value.
Trillia always reads signs from left to right. Order of operations is notated through left-to-right order and parentheses.
Under the hood, `+-` is just a single bitwise operation to set the sign bit, even though it's read by humans as two separate operations.

## 4.4 Bitwise Operations
Bitwise operators are used for low-level control. 
The 8 primary bitwise operations are:

`&`    `~&`

`|`    `~|`

`^`    `~^`

`\`    `~`

The `&` is a bitwise and. The `|` is a bitwise or. The `^` is a bitwise xor.
The `\` is a 'lossy xor'. It's a xor gate for which the base can lose 1's but not gain them.
Here's how it works:

    1100 \ 1010 = 0100
The `\` gate can be read as *"without"*

`~&` is nand, `~|` is nor, and `~^` is xnor. Using `~&` instead of `!&` is done to ensure greater consistency that `~` is *bitwise not*, while `!` is *logical not*.

The `~` operator is a prefix operator, while all other bitwise operators are binary operators.

## 4.5 Some Extra Unary Operators
The unary operators discussed already are the `+` prefix, `-` prefix, `~` prefix, the `+` suffix, and the `-` suffix.
Using `%` as a suffix divides the number by `100` to give a percent.
Using `!` as a prefix changes a component of a logical statement to be the inverse. As in `if a and !b`, which can be alternatively written as `if a and not b`, but `!` affects only what it is prefixed to.
Using `!` as a suffix returns the factorial of that number. So if `g = 4`, then `g!` returns `24`.

## 4.6 Relative Assignment Lines
In Trillia, for any line of code that starts with a variable, and does not assign or reassign that variable, the variable is relatively assigned.

    a + 7 * 2
This takes `a`, adds `7` to it, then doubles it. That's the new value of `a`. If there are multiple variables on a line, such as in `a * b`, then only the left-most variable is reassigned.

# 5. Control Structures
The six comparative operators are: `=`, `!=`, `>`, `<`, `>=`, and `<=`.
These operators return `True` or `False`, and are used to interact most often with conditions.

## 5.1 Branch Control Structures
Trillia supports `if`, `else`, `unless`, and `then`.
The `if` and `unless` keywords are followed by a condition and subordinate code.

    if x = 6
        print(x)
This is an example of an *if block*. The subordinate code `print(x)` is only ever executed if the entire condition is `True`.
In Trillia, it is encouraged that you use the `unless` keyword for negative if statements.

    unless weather = rainy
        go_outside()
The `unless` keyword only activates subordinate code if the expression is `False`.
`unless` is desirable because it makes complicated negations of conditions easier to manage. If there is a mix of positive and negative conditions, the `if` keyword is encouraged for clarity.

The `then` keyword can be used to make subordinate code on the same line, or simply for clarity.

    if is_even(x) then x + 1
or

    if is_even(x)
    then
        x + 1

If you want to execute code only in the case that the condition fails, you can use the `else` keyword.

    if health <= 0
        print("You Died")
    else
        print("You survived a critical hit")

The words can be shifted around and used in different ways as needed to make your code clearer.

    if health <= 0
    then
        print("You Died")
    else
        print("You survived a critical hit")

    if health <= 0 then print("You Died") else print("You survived a critical hit")

A note about optimization:
To provide simplicity and consistency, Trillia does not support `switch`, `case`, `default` keywords for control structures.
Instead, if-else chains are optimized such that if questions are asked using `=`, then the chained `if`s are compiled into a `switch` block for greater speed.

    if x = 1
        do some code
    if x = 2
        do some code
    if x = 3
        do some code
    ...

The Ternary Operator
Trillia has a very simple ternary operator.

    if a then b else c
That's it, and it's no different in syntax than regular if-else statements. You can use the `unless` keyword too.

## 5.2 Reactive Branch Control Structures
Trillia has signals. The when keyword allows you to set a condition that when `True`, jumps code execution to the `when` block's subordinate code.

    day = [`Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`]
    day x;

    when x = Saturday {
        print("Have a good weekend")

    x = Saturday
    }
The `when` keyword requires `{}`s. The braces give signal lifetime. When you exit the braces, the condition is no longer being listened for.

The `when` keyword can be paired with `return`. This means that, much like a `function`, you will be returned back to where you were when the `when` block was called.
If `when` is not paired with a `return` keyword, it will implicitly resume code execution at the place it was where the when keyword was activated.

    when x = Saturday {
        print("Have a good weekend")
        return
    x = Saturday
    }
You can also use the `break` keyword to break out of the `when` block early, starting from directly after the `when` block ends, rather than resuming.

## 5.3 Loops
In Trillia, there are some control keywords that create a loop.
The `repeat` keyword is the simplest looping keyword. If given no value, it will repeat forever, or until the subordinate code encounters the `break` keyword

    repeat
        a + 5
This adds `5` to variable a infinitely

    repeat
        a + 5
        if a > 200
            break
This is a safer way to handle this.

You can give a value to the `repeat` keyword to make it repeat a fixed number of times

    repeat 10
        a + 2
This loop repeats `10` times, then automatically ends.

The `repeat` keyword is especially useful when you want to preserve D.R.Y. (Don't Repeat Yourself).

The second and third looping keywords are `while` and `until`.
The `while` keyword is the same as the `if` keyword except it creates a loop. Every time that loop starts over, the condition is asked again.
The `until` keyword flips the condition's `True` and `False`. `until` is to `while` what `unless` is to `if`.

    while x > 10
        x - 3

    until is_prime(number)
        print(number)
        number + 1

The `while` and `until` keyword can be broken out of using the `break` keyword.
If you use `continue`, on `repeat`, `while`, or `until`, it will jump back to the start of the loop, and re-ask the condition if there is one.

The `do` keyword exists inside loops, and only gets triggered once by default. If you give it a value, then it will repeat that number of times.
The `do` keyword will reset if the loop that it's in is broken out of.

    repeat 20
        do 5
            print("hello world")
        print("memes are funny")
The first five times, it will print hello world. And it will print memes are funny `20` times in total.

Function calls are technically also control structures, but aren't usually thought of in that way.
They unconditionally jump you to another part of the code, and then return you back to where you left off.
In Trillia, you can use the `break` keyword on functions to make them behave similarly to a `goto` statement.

# 6. Debugging
The `?` operator can be appended to a variable to track and print every change that happens to it from that point in the code onward.

    x = 3
    x?        # this line is used to explicitly track x
    while x != 1
        if x /@ 2 then x / 2 else x * 3 + 1

This prints out:
>>> while x != 1 where x = 3 returns True to while
>>> if x /@ 2 where x = 3 returns False to if
>>> else x * 3 + 1 where x = 3 relatively assigns x = 10
>>> while x != 1 where x = 10 returns True to while
>>> if x /@ 2 where x = 10 returns True to if
>>> then x / 2 where x = 10 relatively assigns x = 5
>>> while x != 1 where x = 5 returns True to while
>>> if x /@ 2 where x = 5 returns False to if
>>> else x * 3 + 1 where x = 5 relatively assigns x = 16
>>> while x != 1 where x = 16 returns True to while
>>> if x /@ 2 where x = 16 returns True to if
>>> then x / 2 where x = 16 relatively assigns x = 8
>>> while x != 1 where x = 8 returns True to while
>>> if x /@ 2 where x = 8 returns True to if
>>> then x / 2 where x = 8 relatively assigns x = 4
>>> while x != 1 where x = 4 returns True to while
>>> if x /@ 2 where x = 4 returns True to if
>>> then x / 2 where x = 4 relatively assigns x = 2
>>> while x != 1 where x = 2 returns True to while
>>> if x /@ 2 where x = 2 returns True to if
>>> then x / 2 where x = 2 relatively assigns x = 1
>>> while x != 1 where x = 1 returns False to while
It's very verbose, and goes through every change for which x is either queried or changed.

Using the `?` operator at the end of a line, with a space between it and the last object prints out every evaluation and change that occurs on that line.

    x = 3
    while x != 1
        if x /@ 2
        then x / 2 ?
        else x * 3 + 1
>>> then x / 2 where x = 10 relatively assigns x = 5
>>> then x / 2 where x = 16 relatively assigns x = 8
>>> then x / 2 where x = 8 relatively assigns x = 4
>>> then x / 2 where x = 4 relatively assigns x = 2
>>> then x / 2 where x = 2 relatively assigns x = 1

If you want to monitor every line of code from a starting point to an end point, you can use the `?* *?` debug brackets.
They behave the same as the end of line `?`.

Using `try` and `(catch??? , except???)`, you can make your program behave differently to avoid a crash.

    try x / y
    catch zero_division_error
        print("invalid input")

If your program has a compiler error, you can use `catch` and `ignore` to let your program run anyway.

    catch proven_pointer_cycle_error
        ignore

Because many errors usually result in or are caused by `Undefined` values, and because `Undefined` returns `Undefined` when augmented, this can result in accumulation of `Undefined` variables.

# 7. Reactive Variables
There are four types of reactive variables in Trillia:

Address Pointers: also called Raw Pointers, are the same as pointers in C. Unlike C, however, they are dereferenced by default.
They point to an address of another variable or data structure, and return the value that's held there. Address Pointers are by far the rarest of the four reactives.
Address Pointers are called using the `&:` prefix. You can read `&` as "Address" and `:` as "Pointer". It's literally read in code the same as it's named in English.

    x = &:y
or alternatively:

    x &:= y
This can be read as "x is an addres-pointer to y"

Reactive Pointers: also called Identity Pointers, are similar to Address Pointers, except they never lose track of what they point to.
If a data structure changes address, which is quite common during promotion or data-type change, this pointer is notified, and will reactively point to the new address.
This type of reactive variable is much more common that the Address Pointer because it is much safer, and makes it much easier to maintain stable objects.
Reactive Pointers are called using the `:` prefix.

    x = :y
or alternatively:

    x := y
This can be read as "x is a pointer to y" or "x points to y"
Or, if you want to be more mathematical: "x is defined as y"

Pointer Reactives: also called Lazy Reactives, are actually functions under the hood that re-evaluate every time they are called. They take up no register memory of their own.
They are called Pointer Reactives because they appear nearly identical to Reactive Pointers, except they don't have an address.
Pointer Reactives are called using the `:` prefix; the same as Reactive Pointers.

    x = :y + :z
or alternatively:

    x := y + z
The same syntax appears here as for Reactive Pointers, except there's no reason a programmer would need to re-evaluate for a single value like this.
As a result, the pointer form is single-dependency only, while the reactive form is multiple-dependencies only.
Also, notice that `:=` declares all bare variables as being pointed to. This is shorthand. `x = :y + z` is different from `x = :y + :z`.

Cached Reactives: also called Eager Reactives, are a special type of variable that is given a signal to update every time one of its dependencies change.
The value is cached in memory for later use, and doesn't have to be re-evaluated each call.
Cached Reactives are called using the `$` prefix. You can remember it because cache sounds like cash.

    x = $y + $z
or alternatively:

    x $= y + z
Once again, similar to Pointer Reactives, Cached Reactives have no reason that they would need to be single-element only.
It's technically allowed, but it's best to be avoided.

If a reactive points to an object, and that object is freed or deleted, the pointer will return `Undefined`. An Address Pointer will return whatever value is at the address that it points to.

All of these reactives create dependency chains. If a dependency cycle is detected, your program will error.
If a cycle is provable at compile time, it will give you compile-time-proof-error.
If a cycle is detected at runtime, it will give you a runtime error.

## 7.1 Addressing and Dereferencing
Trillia dereferences pointers by default. This means you're never pulled into the world of addresses unless you deliberately choose to do so.
If you DO choose to enter the realm of addresses, there are three special operators that allow you to do so.

The Address Operator `&` is prepended to a variable to get its address. If prepended to a pointer, it will get the address of the endpoint variable along its dependency chain.

    a := b
    b := c
    print(&a)
This actually gives you the address of c.

If you wish to get the address of a pointer, you can use the `:&` Pointer Address prefix instead. This is also called the "Source Address" or "Name Address" operator.
The Pointer Address operator is designed to only ever give you the address of the exact object whose name you prepended it to. It works on regular variables too.

    a := b
    b := c
    print(:&a)
This gives you the address of variable a.

If you want a pointer to specifically point to the address of a variable, and not be dereferenced automatically, you can use the `&` or `:&` symbol to say so.

    x := :&y
This means that x points to the source address of `y`; not to the value of `y`.

Finally, we have the Dereference Operator `@`. The Dereference Operator gets the value at an address.

    a := &b
    print(@a)
Variable `a` points to the address of `b`, then we print the value at where `a` points to.

You can also use the `@` operator to get whatever's at the address of a literal value:

    print(@1234)
This prints whatever value can be found at address `1234`.

# 8. No Object Oriented Programming or Structs
Yes. That's a good thing. Trillia strives for absolute simplicity, and because we have vectors, and reactives, that's all we need in order to make objects by hand.
This section is not dedicated to a feature, rather, the lack of it.

To create an object by hand, usually, you will want to create a dictionary with reactives that point to other variables in your code.

    player_maximum_health = 100
    player_maximum_mana = 20
    player_equipped_armor = "iron armor"
    player = [[`health`, :player_maximum_health], [`mana`, :player_maximum_mana], [`armor`, :player_equipped_armor]]

This way, every object is crafted by hand, and everything is an `array`, so there is no learning curve. You create arrays in such a way where everything is transparent.
Inheritence is done through reactivity. This is not only clearer, but also faster to compute if done right, and gives more flexability. You can use pointers, pointer-reactives, or cache-reactives to get the exact result that you want.
There is no special `struct` keyword, or special object-oriented syntax. You don't even have to use a dictionary.
It's just a useful tool that helps you get fast lookups while still being highly readable.

    player = [:player_maximum_health, :player_maximum_mana, :player_equipped_armor]
This is what it looks like without it being a dictionary. The only problem is that you need to index it manually, and if elements move around in the array, it could be difficult to maintain.

That's really all there is to it. Objects by hand.

# 9. Automatic Garbage Collection
Trillia's Garbage Collector is extremely simple, and actually so lightweight, that it slightly improves performance rather than impeding it. Here's how:
Trillia's has two Garbage Collectors, and they are entirely separate entities. One of them is entirely designed for non-reactive objects, while the other only handles reactive objects.
The Primary Garbage Collector is compile-time only, and the only thing that it does is insert `free()` operations where it can prove that it's safe to do so.
It frees objects before they are normally freed in the program, either by exiting their scope or when a manual `free()` operation is used.
If the Primary Garbage Collector cannot prove that it's safe to remove an object early, it will move on, and let that object live until the end of its natural scope.
This means that the Garbage Collector never makes your program slower - all data in your program must be freed anyway, and the GC only exists to free it at the earliest possible time.
The Garbage Collector ONLY negatively affects compile time, and it positively affects runtime very slightly by making it easier for the computer to find free space to define new data without cache-misses.
The Primary Garbage Collector has no runtime overhead.

As for the second Garbage Collector - its main purpose isn't actually to collect garbage at all. It's actually a safety-checker for reactive dependecies, that happens to also be perfect for Garbage Collection.
Since the Reactive Safety Checker happens to already be keeping track of which objects point to which other objects, it can mark and destroy objects that are no longer being referenced.
This Garbage Collector technically does take a lot of resources to maintain, however, it has multiple jobs, and the actual Garbage Collection part is a very miniscule module build ontop of its other tasks.
So ultimately, the Secondary Garbage Collector has very little negative effect on performance when only considering the garbage collection portion of it.
This Garbage Collector uses reference counting, and eliminates objects whose reference count reaches 0. It requires both compilation time and runtime.

# 10. Manual Garbage Collection
The `{}` braces are used for scope and namespace. Any object that was created inside of a scope will die at or before reaching the end of its scope.
By default, the `{}` will free() any objects that reach its end. The entire program has a single global scope, which is like an implicit `{}` that surrounds everything.
All functions and threads also have implicit `{}` scope that ends at the return or the end of the function.

If you use `delete {}` then it will delete() all objects that were created within the scope instead of freeing them.

The free() function frees data so the address may be used by other objects instead.
x = 12
free(x)
This destroys x, and frees its address. The value 12 still exists at that memory location, but the Undefined flag is placed on any new object that claims that register.
This means that no new object that claims the memory address that x had, can look at the value that x had.

The zero() function is a function that essentially just wipes the bits of an object. This is useful for resetting an object before it's usurped (more on usurpation later)

The delete() function is the zero() function followed immediately by the free() function. It eliminates all traces of the values that were stored there and then lets that space be used.
This is a good way to get rid of any information that's potentially vulnerable to hacking.

If you use the free() or delete() keywords, the GC will assume you know what you're doing, and will not handle that data automatically.
If you want some data to persist throughout the entirety of a program, instead of being garbage collected during program execution as soon as possible, you can declare it in global space, and manually free it at program end.
This is a good way to ensure that your data isn't constantly slowing down your program while it's being freed. However, it comes with the cost of wasting extra memory during program run.

The is_free() function is used with an address as the input, and it returns whether that address is available for the taking or not.

## 10.1 Usurpation and Manual Address Assignment

During Declaration of an object, you can use the @ symbol to manually set where that data is supposed to go.
int32 @1234 x = 24
This creates variable x at address 1234, and sets the value to 24.

The @ operator can be used to usurp other objects.
int32 y = 30
int32 @&y x = y
The '@&y' is read as "at the address of y"
This "creates" a new variable x, in the space where y is, killing y, then it "assigns" x's value to y's value.
What this does, under the hood, is essentially just renaming y. And there's an optimisation that happens with "@&y" + "= y", which is just that x is never given the Undefined flag.
If we don't say "= y" at the end, the variable x will steal the position that y had without being given access to its value. X will be flagged as Undefined.
Destroying objects by taking their place is called "usurpation".

The ()evict() and ()displace() functions are also useful too.
(q)evict(r) is a function that creates q at r's position, and tells r to take a hike. This moves r to a new position.
(q)evict(r, s) is a function that creates q at r's position, and tells r to take a hike. This moves r to a new position. Object r now goes to address s.
To chain evictions together, you can do so with the function-chaining syntax: (a)evict(b)evict(c)evict(d). d is evicted at the end, and will go wherever is available.

The ()displace() function takes in an address as its right-hand argument. Then, if there is an object there, that object is displaced and moved elsewhere.
The same as the evict keyword, you can chain the ()displace() function too.

You can use these special functions during declaration to place a variable in memory exactly how you wish, without having to first place the variable randomly
int32 evict(y)evict(z) x = 32        # The exact syntax here is a bit undecided, but this is the idea.

# 11. Functions
Functions in Trillia, are blocks of code that can do a specific task whenever it is called.
Here are an examples of function definitions:

hello_world() =
    print("hello world")

(a)add(b) =
    return a + b

collatz(n) =
    while n > 1 then if n /@ 2 then n / 2 else n * 3 + 1

(n)collatz =
    while n > 1
        if n /@ 2
            n / 2
        else
            n * 3 + 1

Functions can be right-handed, left-handed, or ambidextrous.

Right-handed functions are return-only and have no side-effects.

Left-handed functions are what most other computer programming languages call 'methods'. They alter an object

Ambidextrous functions alter an object, but have right-handed inputs that affect the manner in which the alteration occurs.

For relative assignment lines:
x + 5
You can use left-handed functions to relatively assign what is to the left. This chains naturally, and keeps the statement as an assignment line.
In Trillia, left-handedness is associated with augmentation of values, while right-handedness is associated with having no side-effects.
This is the dichotomy between pure functional programming vs object augmentation.
Trillia allows and encourages both, because there are times when one is slightly faster for optimization, or times when one is more readable.
Trillia gives you the choice, and you can change between these styles freely.
(((my_array)sort)append(y))pop(4)

((x)add(10))multiply(20) + 5
This entire line is a relative assignment of x.

To assign a name to a function, you can do this:
my_first_function() =
    print("hello world")

my_second_function() = my_first_function


## 11.1 Function Nesting
((a)append(b))append(c)

========================

## 11.2 Function Chaining
If you chain functions, the left-handed object undergoes the first function, then the result becomes the left-handed object for the next function.

    (a)append(b)append(c)
Here, b is appended to a. Object a is altered, then c is appended to a.

((a)append(b))append(c)        --- difference??? ma?
maybe it ought to be such that (a)append(b)append(c) is where (a)append(b) and then (b)append(c) ne?

=========================



# 12. Threads
The `thread` type is a type of function and a type of vector. Essentially, a thread is to a function what an array is to a variable.

thread2 x(input_array) =
    Just try to make a thing where they meet in the middle.

Threads, like functions, can be right-handed or left-handed. Except with threads, right-handedness and left-handedness have additional meaning.

For threads, right-handed inputs also mean that the input is locally copied to each thread.

For left-handed inputs, it means that the input is globally shared among the threads, and it will undergo an augmentation queue.
This is not reccomended, but for some tasks it may be difficult to avoid.

All variables that are defined inside of a threaded function are defined as local variables by default.
To make a variable only belong to one thread, or to share them often breaks determinism, so it's very much discriminated against, but it is allowed. Here's how:
thread10 my_thread =
    if thread = 1
        x = 12
This only ever creates the variable x for the first thread. variable x is never created in any other threads.

If another thread is to access that thread's x variable, they must say:
if x in thread[1] > 10
    do some code
They must explicitly mention which thread that variable belongs to. This can absolutely cause problems if not paired with awaits.

If a const variable is accessed in threaded function, that variable is read-only, which means that there will be no queues required to access it.

The await keyword passes a core along to another thread if there are other threads available to adopt that core.

You can create a busy loop by using when + await to do busywork while waiting for a signal.

Using left-handed inputs allows you to mutate objects in global scope. But, with a few rules. And normally, you are not allowed to write to global scope.
When an object enters a threaded function as a left-handed input, it tells the program that the object belongs to that function, and is not allowed to be mutated by anything else while the thread is active.
To access the object, you must do this:
thread3 (meme)super_cool() = 
if thread = 1
    mutation permission to thread[1]
    await write to meme in super_cool
Something *like* this is how it should work. This still isn't enough to ensure determinism, but it is a start.

The only way to make this work is if we have a model that gives permission like hot potato, deliberately, OR assign one thread to be the
only thread that owns an object, and feed that thread other thread's info as needed.









Maybe I should just have it "await read of x by thread[10]" without an '_'.
await_read and await_write
await_write unto x in thread[3] / of x in thread[3]
await_write unto x by thread[2] / unto x from thread[2] / of x by thread[2] / of x from thread[2]

What about change of global state???

Thread-mating
If a thread is awaiting another thread to read from it or write to it, then it is called a submissive thread
If a thread is awaiting another thread so that it can write to it or read from it, then it is called a dominant thread


await read is faster than await write. Await read actually creates a temporary constant variable that can be safely read by the other thread. Await read actually doesn't stop the thread from moving.
await read is also very likely discouraged because you can make constants instead, and make it so they're read without need of explicit sharing via mutual awaits.

Maybe await write should actually also let the thread continue as far as it can go before it has to mutate that awaited variable.
Once it encounters any code inside the thread that changes the awaited variable, it waits for the writer to change it before making the change.

You can await multiple things, but the order that the awaits have to be resolved in is in FIFO order.
await read of x in thread[2]
await read of y in thread[2]
here, x has to be read first, then y. 



There is also permit read and permit write
x = 10
permit read of x from my_function
This is usually used for global scope. It's essentially an ownership model.
To "undo" it, you simply says "permit read of x"



Thread object ownership model. To ensure deterministic writing capabilities, any non-local object to a threaded function must be imported.
Importing higher-scope-objects is done via left-handed thread inputs. (a)my_thread makes the object a become owned by the threaded function.
The object a cannot be altered from any other source while the threaded function is still ongoing.

Any object that is owned by a threaded function, must undergo a second step of being owned by a specific thread.
permit write unto a by thread[6]






What about read-only threads? and threads not returning, or returning None.
For example, we might not want every thread to return a value

How exactly are threads even exited? What I had before was once all threads return or reach the end, but it might be more funky than that.









========================================


# 13. If Statements for Assignment




confusion between = and =
x = y = z;
In C, this is actually even less intuitive. Is it (x = y) and then (y = z), or is it y = z and then x = y?
I'll tell you. It goes from right to left.
In Trillia, the first = is an assignment of x, while the second one is a comparative operator.
x = y > z
Might make it easier to understand. You can use `if` to be more clear.
x = if y = z
Here, the `if` actually gets the value of the expression as True or False, and that is then returned to x.
Maybe `if` should be enforced here for clarity. hmmm...
Yeah, the if is enforced!


Normally, if you just have a line of code that calls a variable, but does nothing with it, you'll get a redundancy error, and the error handler will tell you to clean it up.
my_var
This would error immediately

For the case of 'if' having values that return to nothing.
If you have an if statement like this:
if a = b
then c

here, normally, c would just be a variable whose value is returned into the void (causing a redundancy error).
However, for conditionals like if and unless; if there is a value that's returned into the void, it's actually returned back to the if statement itself.
This way, you can have:
a = if b = c then True else False
Normally, True and False would be returned to no object, but because they belong to an if block, they're returned to it instead.
This will still cause an error if nothing is there to catch the returned value of the if
If you're using an "if" as an assignment, you can chain many "if"s together, but every if must be paired with an else statement to prevent missing assignments, and each branch must give a return value back to the if.
You can have a = if b = c, and that will be valid because b = c is returned to if as True or False. The final resolved value that is returned to the if when the expression is done with branching is the value that if returns back to the assignment operator.

a cool thing about the = inside of if statements is that, oddly, it actually CAN be used for assignment.
a = if b = c
This is a valid statement. It defines a based on whether b and c are equal.

# 14. Naming Conventions


# 15. Libraries and Imports
Standard library uses automatic imports as needed, everything else needs manual imports
The unsafe library is the only official library that is not given by default. It allows you to do some extra things like revive()

# 16. Trillia on C or C++
The Language on C - c_ asm_... talk abour c_ and x86_64_ and arm64_





# 17. Trillia's Virtual Memory Machine
Trillia has a very different address system than what you are used to. To ensure full determinism, virtual memory is managed by Trillia entirely.
Memory is indexed as a large vector. EVERYTHING IS A VECTOR DAMNIT!!!











Should I allow:
int32, nat32 x = 20
A more customized way of creating duck-typing or unions

Talk more about function chaining. Work out the kinks in the system (a)append(b)intersection(c)

Go through a thorough process of dissecting what threads really need to ensure determinism.
1. Left handed threads are necessary for the threaded function to claim ownership of global objects.
2. you need to grant permitions to change a thread-owned object before you can mess with it. Each object can be tossed around separately
3. Really understand if this is deterministic or not. Really get into the weeds. If it's not, then make a single thread only be able to affect the object, and disallow permission passing.
permit write to x by thread[y]. Permissions must be one at a time. Once the thread is destroyed, permission is automatically granted globally.

Consider the possibility of custom iterable types.
set = []
and then allow the custom set type to be mutated in only very specific ways.

Think about dictionaries a bit more. What exactly are they? Are they definitions of enums in and of themselves, or do/can they use pre-existing enums?






Talk about strings. We literally just breeze past them.
Talk about comments.
talk about ()func() syntax. It's chosen because it's more consistent. A beginner doesn't have to think about a.b(c) syntax. it's always (a)b(c).



