Trillia

Trillia is a computer programming language inspired by C, Python, Go, and Lua, with the purposes of ensuring maximal simplicity, readability, consistency, and rapidity of onboarding.
The Implementation of Trillia is language agnostic. It doesn't matter which languages are used, and it also doesn't matter whether Trillia is transpiled, compiled, or interpreted, as long as it behaves the same.
The An ideal Trillia implementation would be a boostrapped Trillia that compiles to C or C++. This is because C is very low level, unrestrictive, and has many libraries and modules.
Trillia should also always have full access to functions, libraries, and keywords of the language that it compiles to to ensure maximal tooling.

Some notable features are:

1. Whitespace
Trillia is whitespace significant. Indentation replaces the need for brackets, and new line characters replace the need for semicolons. This ensures minimalism.
If you wish to have multiple statements on a single line of code, or just wish to be explicit, you can use ; as an alternative. There are certain occations where ; is reccomended for clarity.
If you wish to have a single statement be split across multiple lines, you can use ;; to nullify the \n new line character. This ensures that you can more easily represent matrixes in your code.
Indented code is called subordinate code, and the code that is dedented above that subordinate code is called ordinate code. Indents are 4 spaces.

2.0 Variable Assignment
Variables are assigned using a variable name, followed by the = sign, then the value you are assigning to it
x = 10

2.1 Strict Types and Sizes
If you don't use types, the variable will automatically promote or change type readily as needed. You can use strict types and sizes to ensure that the variable does not change type or size.
int32 x = 10

If you use a type without a size, the type of the variable will remain consistent, but size promotion and demotion will occur when necessary.
int x = 120     # this is an 8 bit integer by default
    x = 300     # It was promoted to a 16 bit integer to be able to represent this value.

If you use the scal type (short for scalar), you can set a size but not a type. This is the same as a union in C.
scal64 x = 4800
       x = -0.3333

You can use the scal type without a size to explicitly state that a variable is intentionally dynamic type and size instead of being a hastily programmed prototype.
scal x = "hello"

2.2 Mutability
There are four keywords that change which ways your data is allowed to be altered.
The const keyword, alternatively written as constant, will prevent your data from being altered.
The stat keyword, alternatively written as static, will only allow your data to be assigned or reassigned but not altered or relatively reassigned.
The rel keyword, alternatively written as relative, will only allow your data to be relatively reassigned or altered, but not assigned.
The mut keyword, alternatively written as mutable, will allow your data to be altered in all ways.

2.3 Declarations
If you wish to claim memory before assigning it a value, you can declare without assignment. It's reccomended that you use ; for clarity, signalling that you intentionally did not provide assignment.
int32 x;

If you have a variable with mutability restrictions, you can use a declarative line on that variable with a new mutability rule to specify a deliberate change in mutability.
mutable x;

If you wish to cast the type and or size of a variable into another type, you can also do so by using a declarative line.
nat32 x;
This is only possible if the value can be perfectly preserved. Floating points can error.

2.4 Hard Variables
Using the hard keyword, variables can be stored as writes to another file. Trillia files that you program in are labelled X.tri, where X is the name of your program.
If a hard variable is created, an X.trihard file will be created automatically to contain all hard variable data.
Hard variables are much slower to assign or alter, but they are saved variables that don't require you to use read() or write()

A special case:
If you use hard + const, you get a literal value that is treated as a variable.
hard const rat32 PI = 3.1415
Here, the value of pi is stored in your program at compile time. It's very similar to #define in C.

3.0 Types
Different data types are used best for different tasks. 
Trillia has four numeric types: nat, int, rat, and float. All of these are suffixed by the number of bits used to represent them.
All of the numeric types are suffixed by the number of bits used to represent them. For example, natX is most often in the forms nat, nat0, nat8, nat16, nat32, and nat64.

3.1 Numerics
Natural numbers "nat" are what most other languages call 'unsigned integer'. The nat type is the most basic form of numeric data type.

Integers "int" allow negative numbers to be represented.

Rational numbers "rat" are actually an array of two numbers, a divisor and denomonator, that exist as a reduced fraction in memory. The size represents the size of both elements in the array.
The rational type is preferred over floating point where precision is more valuable than speed.

Floating point numbers "float" are exactly the same as floats usually are in other languages.

Next up is the Scalar type "scal", which is also notated in bits.

3.2 Built-in Symbolic Types
The next types are non-numeric, and have only one size.
char is 8 bits, used to represent characters in strings. They use ascii.
bool only has two literal values, True or False.
Undefined is the default value of any variable that has been declared but not assigned. If a read occurs on a value that is Undefined, it will cause an error.
None is similar to Undefined, except it is used to explicitly return an empty value. This doesn't crash upon read.

3.3 Vector Types
The vector types are: vecX, arrayX, listX, and threadX.
Vectors are suffixed not by number of bits, but instead by number of elements that they have. For example, array4 holds 4 elements.
Vectors exist in two flavors: arrays and lists.
Using the vec type, Trillia will create an array if possible, and a list if not. The vec type is best to use in most instances.
Using the array type, Trillia will attempt to create an array, and if the elements do not conform to the rules of arrays, an error will occur.
Using the list type always creates a linked list.
The thread type is a special type of vector. More about it later in the Threads section.

Trillia doesn't support sets, tuples, dictionaries, maps, or any other type of iterable. You make them yourself, and specify their rules.
There are many built-in functions that are best used for sets, such as union() or intersection(), and guidelines on which functions to use, but no hard rules.

3.3 Custom Symbolic Types (Enumerations)
Custom data types are defined using a name for the type, followed by the = sign, followed by an array, of which, each element is encapsulated with \` markers, similar to strings.
fruits = [`apple`, `orange`, `banana`, `plum`]
The backticks are used in the same way as strings, but unlike strings, the entire word used is treated as a literal, individual characters cannot be indexed, and they take up far less memory than strings.
The individual elements do not behave like numerics, but they can be accessed by index. Ultimately, you define the rules in which each symbol is used.
For example, you cannot say apple + apple and expect orange to be the return value unless you specifically define that to be the case.

4.0 Symbols and Operations
Trillia makes use of keyboard symbols to perform common operations.

4.1 Symbol Spacing
Trillia is very strict about using spaces when using symbols. This ensures greater readability.
Some symbols change meaning depending on where they are placed, so clarity through spacing is both important and enforced.
For example, + can mean "positive" in +10, "addition" in 23 + 45, and "increment" in 6+.
There are four main symbol types:
Prefixes
Suffixes
Binary Operators
Brackets

All prefixes must be prepended to what they modify. All suffixes must be appended to what they modify. All binary operators require at least one space before and after what they modify, and brackets must be opened and closed.

4.2 Order of operations
In Trillia, the order of operations is always brackets first, left to right. There is no higher precedence given to multiplication over addition, or certain functions over others.
2 + 5 * 10 returns 70. If you want it to be done in proper order, just move things around or use brackets.
5 * 10 + 2   returns 52
2 + (5 * 10) returns 52
If there are multiple disconnected brackets in a larger expression, if your version of Trillia is implemented with automatic parallel threading, it should understand that it can solve for both pairs of parentheses at the same time.
(1 + 2) + (3 + 4)
(3) + (7) # both sides were solved simultaneusly.
If there are more brackets to solve in parallel than there are cores on your computer, left-most brackets are resolved first to preserve left-to-right execution.

4.3 Arithmetic Operator Symbols
For Arithmetic, Trillia has seven binary operations. You do not have to import a math library to access pow(), sqrt(), or log(); these operations are built into the language as symbols, and are intuitive to use.
+ Addition
- Subtraction

* Multiplication
/ Division

** Exponentiation (Powers)
// Radication (Roots)
\\ Logarithmatization (Logarithms)

The symbols chosen for roots and powers are the same as the symbols for multiplication and division. The symbol for logarithms is just a mirroring of the symbol for roots.
With a system like this, you don't have to remember individual symbols, you just need to remember rules.
If eventually computers are capable of much faster calculations and representing larger values, ***, ///, and \\\ can be used for tetration and its root and log equivalents.

The notation of binary operators is:
base operation modicand = return_value
So in the expression "1 + 2", 1 is the base, 2 is the modicand, + is the operation, and 3 is the return value.
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
This expression would error because 2/3 gives a non-integer return value.
To avoid this, there are different types of division.

To round your division up, down, or nearest, use /^, /_, and /~ respectively.
int a = 2
int b = 3
a = a /  b     # This errors because a is an integer and a / b returns a rational.
a = a /^ b     # a = 1
a = a /_ b     # a = 0
a = a /~ b     # a = 1. In the case of 0.5, it rounds up.

There are also two more forms of division, /% and /@.
The /% is modulo division. It divides, and returns the remainder instead of giving a fraction.
a /% b     # This would return 1

The /@ can be literally read as "divides at" or "is divisible by". Instead of returning a number, it always returns True or False.
my_variable = a /@ b
For this expression, my_variable would be False.
The /@ operator makes the common "a % b == 0" or "a % b != 0" expressions - that are often seen in other languages - shorter, and more readable.

Exponents are non-commutative. The modicand is always the "little number" that you see in "x squared" or "x cubed"
2 ** 3 = 8
3 ** 2 = 9
This can be read as "two to the power of three is eight"

Roots are written in the same way, where the exponent is the modicand.
This can seem slightly confusing at first because common notation puts the exponent on the left for roots, but in Trillia, the modicand is always the exponent.
100 // 2 = 10
25 // 2 = 5
This can be read as "twenty five to the root of two is five"
Also, notice that with this notation, there is much more freedom than sqrt() and cbrt() because you are not limited. You can choose any exponent that you want, not just 2 or 3.

Roots also come with variant operations: //_, //^, //~, //%, and //@.
The //_, //^ and //~ operators round the result down, up, and nearest respectively.

The //% operator returns the remainder of a root.
10 //% 2 = 1
because 9 // 2 = 3 exactly, and 10 is 1 more than that.
Some more examples to get the hang of it:
27 //% 2 = 2
16 //% 2 = 0
99 //% 2 = 8

The //@ operator is basically an "is_square()" or "is_cube()" function that returns true if the base is a power of the modicand.
100 //@ 2 = True
70  //@ 9 = False

Logarithms are the same as roots, except the return value and the modicand are swapped.
100 \\ 10 = 2
25 \\ 5 = 2

To get natural logarithms, you can use the built-in EULER constant as the modicand
10 \\ EULER = 2.30258509299

The same variant operators exist for logarithms as do exist for division and roots. \\^, \\_, \\~, \\%, \\@.
The \\^, \\_, \\~ operators round as expected.
17 \\@ 12 = False
10 \\% 3 = 1

Incrementation and Decrementation:
As a final note on arithmetical operators, the suffixes + and - are able to be used for adding or subtracting 1 from a value.
10+ = 11
79- = 78

You can chain these together
3++  = 5
0--- = -3

To prevent redundancy, and to increase readability, chaining + with - directly is not allowed.
10++--- # this gives an error, because 10++--- can be refactored into 10-.
Under the hood, chaining +'s or -'s in long strings is simply condensed into addition. So 5+++++ is just 5 + 5 to prevent wasted operations.

Positive and Negative:
As a prefix, + makes what it affects always positive. It is an absolute value unary operator.
+12
g = -50
h = +g # variable h is now 50.

As a prefix, the - sign always flips the sign from positive to negative, or negative to positive.
g = -50
h = -g # variable h is now 50.

For literals, you can only have a single + or - sign as a prefix. --4 is not allowed because it can be reduced to 4, or +4 for clarity.
For variables, no sign, +, -, and +- are all allowed.
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
A + sign means you're taking the absolute value of the variable. This ensures you will get positive value.
A - sign means you're flipping the sign of the value of the variable. This ensures you will always get the opposite signage of the variable.
The +- means you're doing +, which makes the value of the variable positive, and then -, which flips the sign. This ensures you will always get negative value.
Trillia always reads signs from left to right. Order of operations is notated through left-to-right order and parentheses.
Under the hood, +- is just a single bitwise operation to set the sign bit, even though it's read by humans as two separate operations.

4.4 Bitwise Operations
Bitwise operators are used for low-level control. 
The 8 primary bitwise operations are:
&    ~&
|    ~|
^    ~^
\    ~
The & is a bitwise and. The | is a bitwise or. The ^ is a bitwise xor.
The \ is a 'lossy xor'. It's a xor gate for which the base can lose 1's but not gain them.
Here's how it works:
1100 \ 1010 = 0100
The \ gate can be read as "without"

~& is nand, ~| is nor, and ~^ is xnor. Using ~& instead of !& is done to ensure greater consistency that ~ is bitwise not, while ! is logical not.

The ~ operator is a prefix operator, while all other bitwise operators are binary operators.

4.5 Some Extra Unary Operators
The unary operators discussed already are the + prefix, - prefix, ~ prefix, the + suffix, and the - suffix.
Using % as a suffix divides the number by 100 to give a percent
Using ! as a prefix changes a component of a logical statement to be the inverse. As in "if a and !b", which can be alternatively written as "if a and not b", but ! affects only what it is prefixed to.
Using ! as a suffix returns the factorial of that number

4.6 Relative Assignment Lines
In Trillia, for any line of code that starts with a variable, and does not assign or reassign that variable, the variable is relatively assigned.
a + 7 * 2
This takes a, adds seven to it, then doubles it. That's the new value of a. If there are multiple variables on a line, such as in a * b, then only the leftmost variable is reassigned.

5. Control Structures
There are four types of control structures in Trillia:
Branch
Jump [fn(), continue, ]
Loop [while, until, repeat, do]
Exit [break, return]

5.1 Branch Control Structures
Trillia supports if, else, unless, and then.
The if and unless keywords are followed by a condition and subordinate code.
if x = 6
    print(x)
This is an example of an if block. The subordinate code "print(x)" is only ever executed if the entire condition is True.
In Trillia, it is encouraged that you use the unless keyword for negative if statements.
unless weather = rainy
    go_outside()
The unless keyword only activates subordinate code if the expression is False.
Unless is desirable because it makes complicated negations of conditions easier to manage. If there is a mix of positive and negative conditions, the if keyword is encouraged for clarity.

The then keyword is used for making subordinate code on the same line, or simply for clarity.
if is_even(x) then x + 1

if is_even(x)
    then x + 1

If you want to execute code only in the case that the condition fails, you can use the else keyword.
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
To provide simplicity and consistency, Trillia does not support switch, case, default keywords for control structures.
Instead, if-else chains are optimized such that if questions are asked using =, then the chained ifs are compiled into a switch block for greater speed.
if x = 1
    do some code
if x = 2
    do some code
if x = 3
    do some code
...

5.2 Reactive Branch Control Structures
Trillia has signals. The when keyword allows you to set a condition that when True, jumps code execution to the when block's subordinate code.
day = [`Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`]
day x;

when x = Saturday {
    print("Have a good weekend")

x = Saturday
}
The when keyword requires {}s. The braces give signal lifetime. When you exit the braces, the condition is no longer being listened for.

The when keyword can be paired with return. This means that, much like a function, you will be returned back to where you were when the when block was called.
when x = Saturday {
    print("Have a good weekend")
    return
x = Saturday
}

You can also use the break keyword to break out of the when block early, starting from directly after the when block ends.








X Low Level Pointers, Addresses, etc
pointers use the : prefix for what variable is being pointed to.
Pointer addresses use :&
Addresses use &
x = :y # x points to y.

x gives the value of y
y gives the value of y
&x gives the address of y
&y gives the address of y
:&x gives the address of x
:&y gives the address of y

@1234 is the opposite of the & operator. it is the address 1234. You can do a lot of cool things with it.
x = :y       #this says that x points to y. x actually references the variable y itself, not the address of y. If the address of y changes, x will still point to y. This is why it is a reactive pointer, not just a pointer. It's by identity, not by address.


b = 6
print(&b)    # this prints 1234
print(@1234) # this prints 6
# maybe * might be different. Idk.


free() doesn't reset the bits of an object. It kills a variable and marks the register as free for the taking.
zero() resets all bits in a register or structure to 0. This is faster than delete if you want to usurp addresses using @&.
delete() is just zero() and then free(). This is used when you don't have an inheritor in mind, but you want the data to be cleared - usually for safety reasons.
is_free() returns True if an address is available for taking without need to usurp it.
namespace "{}" and "delete {}" to free and delete all objects.



------------

Using the @ operator for definition or declaration can be super useful.
int32 x = 24
int32 @&x y;
This means we now have a variable y that claims the register at x's address.
"at the address of x, declare a variable y"
This moves ownership of x's data directly to a new variable, y.
This kills variable x in the process.
You can use @1234 to define a variable "at" address 1234.


@&. (a)usurp(b) a kills b and inherits all belongings. It's the same as renaming, but also with additional functionality that it can be used to manually place data where you want.
(a)evict(b). b is a reference, like a variable name. a steals b's spot and b has to move somewhere else.
(a)displace(b). b is an address. a says "if there's something here, it has to move out of my way and go somewhere else". There is no guarantee that something will be there.
we can use usurp address and usurp &var
we can use displace address and displace &var

if a pointer points to a variable, and that variable gets freed, what should happen?

own()
borrow()
disown()
lend()
give_back()
share()
revive() or something - it can clear the Undefined flag without assigning a new value. Might call it something else.




X Reactivity
Pointers
Lazy Reactivity
Cached Reactivity
Signals

Debugging + try catch

The unified = sign
    a, b = b, a #swap values just as in Lua.

X Control Structures
if, else, then, unless, keywords

X Functions
Right-Handed Functions
Left-Handed Functions (talk about relative assignment too here)
Ambidextrous Functions
assigning names to functions

Y Parallel Threads
Parallel Threading
Right handed and left handed threads
const keyword makes variables shared. This is because const is read only.

X Garbage Collection and Memory Management


Guidelines and additional rules:
Naming
Whitespace for +X, +, and X+
Standard library uses automatic imports as needed, everything else needs manual imports
No OOP, no structs
The Language on C



X Automatic Garbage Collection: 
Trillia's GC is compile-time only.
There is no extra overhead, no reference-tracking, except likely for pointers and reactives, which already have most of the reference-counter and reference tree systems already built-in to prevent cyclical dependencies.
The GC collects only what data can be provably unneeded. It calculates this during compile time, and if it cannot prove that an object is able to safely be destroyed early, then the GC does nothing, and lets it be destroyed at the end of its scope naturally.
Somewhat paradoxically, Trillia's GC actually improves runtime speed very minutely rather than slowing it down. This is because there are more empty slots in memory available to place new objects, which makes it more likely to hit freed memory.
Essentially, the GC has no runtime overhead. Unreactive objects are destroyed based on lifetime or provable compile-time analysis, and reactive objects use dependency chains that are already necessary to prevent cyclic dependencies.
The runtime safety checker (RTS) handles all reactive objects, and frees them at runtime when the number of references = 0.
The safety checker is needed to prevent cycles and other dangerous code, and it also just so happens that the same systems used for safety are also needed for GC of reactive objects.
The RTS adds overhead, but it's not primarily a GC, and its GC processes don't add any extra overhead.
This means that all GC in Trillia adds 0 extra overhead, and oftentimes due to memory allocation searches, Trillia's GC actually speeds up execution time very slightly instead of slowing it down.





Chart of things that you can define using = :
variables
arrays
lists
functions
threads      (vectors)
enums        (vectors)
pointers
pointer reactives
cached reactives


















