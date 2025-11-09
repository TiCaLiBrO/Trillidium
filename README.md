Trillia

Trillia is a computer programming language inspired by C, Python, Go, and Lua, with the purposes of ensuring maximal simplicity, readability, consistency, and rapidity of onboarding.

Some notable features are:

1. Whitespace
Trillia is whitespace significant. Indentation replaces the need for brackets, and new line characters replace the need for semicolons. This ensures minimalism.
If you wish to have multiple statements on a single line of code, or just wish to be explicit, you can use ; as an alternative. There are certain occations where ; is reccomended for clarity.
If you wish to have a single statement be split across multiple lines, you can use ;; to nullify the \n new line character. This ensures that you can more easily represent matrixes in your code.

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
Custom data types are defined using a name for the type, followed by the = sign, followed by an array, of which, each element is encapsulated with `` markers, similar to strings.
fruits = [`apple`, `orange`, `banana`, `plum`]
The backticks are used in the same way as strings, but unlike strings, the entire word used is treated as a literal, individual characters cannot be indexed, and they take up far less memory than strings.
The individual elements do not behave like numerics, but they can be accessed by index. Ultimately, you define the rules in which each symbol is used.
For example, you cannot say apple + apple and expect orange to be the return value unless you specifically define that to be the case.








X Operations

X Order of operations

The unified = sign

X Control Structures
if, else, then, unless, keywords

X Functions
Right-Handed Functions
Left-Handed Functions
Ambidextrous Functions

X Reactivity
Pointers
Lazy Reactivity
Cached Reactivity
Signals

Y Parallel Threads
Parallel Threading

X Garbage Collection and Memory Management


Guidelines and additional rules:
Naming
Whitespace for +X, +, and X+
Standard library uses automatic imports as needed, everything else needs manual imports
No OOP, no structs
The Language on C











