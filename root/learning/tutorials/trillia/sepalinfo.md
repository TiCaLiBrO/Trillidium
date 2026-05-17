# Course 1: Trillia

This course teaches the fundamentals of Trillia.
Really, it teaches the entirety of base Trillia, which is the programming language with nothing added.
The only extra thing that *is* added on top is output.
This is because output is **extremely important** for fixing your code and learning about what's actually happening inside your program.
This course teaches absolutely everything that Trillia can do without any extra tools.
Except for course 0, all other courses require that you complete this course first.

### Chapters

Below are all of the chapters in the Trillia course.
Chapters, much like courses, are numbered and have prerequisites.
Completing each chapter numerically is the optimal route to unlock as many of the other chapters as quickly as possible.
You are not expected to, and should not adhere strictly to the numbering, but you should complete all requirements before entering a chapter.
The courses are structured to be flexible, allowing students to learn things that interest them early on.

> [!TIP]
> If you see a chapter that interests you, learn the prerequisite chapters and go straight for it. Learn what you want when you want.

Before you begin, these lessons are mostly intended to be done in SEPAL, not Trillia proper.
If you're reading this inside the terminal, then you're inside SEPAL already.

> [!WARNING]
> **Do not exit SEPAL or write your code in a code editor unless instructed to or unless you know what you're doing.**

## Chapter 1 Printing

[/printing](https://github.com/TiCaLiBrO/Trillia/blob/main/root/learning/tutorials/trillia/printing/sepalinfo.md)

Requirements:

- None

Chapter Summary:
	*This chapter is the very first chapter.
	Here, you will learn the most important skill that you will ever learn as a developer: printing.
	Why is it so important?
	Because it's the main way that programmers can learn about what's actually happening in their code if they make a mistake.
	It's the gateway to see inside your computer.*

New Vocabulary:

- print()
- printn()

////(4 lessons thus far)





















////////////////////////////////////////////////////////////////////////////

[[Introduction to Trillia Chapter 2 Variables]] (7 lessons thus far)
Requirements:
- Chapter 1
New Vocabulary:
- `_=_`, `,`

[[Introduction to Trillia Chapter 3 Comments]] (3 lessons thus far)
Requirements:
- Chapter 1
New Vocabulary:
- `#...`, `...##`, `#*...*#`

[[Introduction to Trillia Chapter 4 Arithmetic]] (30~ lessons thus far. We might break arithmetic into three chapters: Beginner Arithmetic (`+`,`-`). Intermediate Arithmetic(`*`,`/`), Advanced Arithmetic(`**`,`//`,`\\`))
Requirements:
- Chapter 1
New Vocabulary:
- `+_`, `-_`, `_+_`, `_-_`, `_delta_`, `_*_`, `_/_`, `_`, `^`, `~`, `_/%_`, `_%`, `_**_`, `_//_`, `_\\_`

[[Introduction to Trillia Chapter 5 Debugging]]
Requirements:
- Chapter 2, 3, 4
New Vocabulary:
- `_?`, `??`, `?*...*?`

[[Introduction to Trillia Chapter 6 Conditions]]
Requirements:
- Chapter 5
New Vocabulary:
- `if`, `then`, `else`, `unless`

[[Introduction to Trillia Chapter 7 Reactivity]]
Requirements:
- Chapter 5
New Vocabulary:
- `:_`, `_:=_`

[[Introduction to Trillia Chapter 8 Logic]] (True, False, Undefined, None, Help, and Error)
Requirements:
- Chapter 6
and or not is `_/@_`

[[Introduction to Trillia Chapter 9 Functions]]
Requirements:
- Chapter 7
// Return functions (handled later, in complex control???)
// Right-handed Functions
// Left-handed Functions
// maybe we ought to split these up. also do ordinal programming and cardinal programming.
// first-class functions (functions being able to be used as objects or variables)
// higher-order functions (functions being able to return other functions)

[[Introduction to Trillia Chapter 10 Recursion]]
Requirements:
- Chapter 8, 9
RECURSION
repeat do

[[Introduction to Trillia Chapter 11 Lists]]
Requirements:
- Chapter 10
for from to where has in within after at before end first last start previous next all any only

[[Introduction to Trillia Chapter 12 Bitwise Operations]]
Requirements:
- Chapter 8

[[Introduction to Trillia Chapter 13 Scope]]
Requirements:
- Chapter 5
as

[[Introduction to Trillia Chapter 14 Complex Control Structures]] (break, continue, return)
Requirements:
- Chapter 10
COMPLEX CONTROL
break continue return

[[Introduction to Trillia Chapter 15 Setwise Operations]]
Requirements:
- Chapter 11, 12

[[Introduction to Trillia Chapter 16 Local Objects]]
Requirements:
- Chapter 13
local

[[Introduction to Trillia Chapter 17 Custom Types]]
Requirements:
- Chapter 8, 11

[[Introduction to Trillia Chapter 18 Pointers]]
Requirements:
- Chapter 11, 14

[[Introduction to Trillia Chapter 19 Interrupts]] (Error, Help, try, when)
Requirements:
- Chapter 13, 14
INTERRUPTS
catch try when

[[Introduction to Trillia Chapter 20 Inheritance]]
Requirements:
- Chapter 15, 16
self





///////////////////////////////////////////


// Cardinal Programming (Pure Functional Programming) (pure)
- pure

// Ordinal Programming (Mutation and Side Effects) (relative)
- relative

// Read Only Objects (constant)
- constant
- mutable

// conditional comments (for testing, debugging, unit tests, and so on) `code ## condition` and `#* code *# condition` Requires chapter 8 and 14.
// Write Only Objects (maybe only allowed inside of the Q library)
// `main` needs to exist, but it also needs to be its own library. This is because it grants your program a single instance of pre-runtime input. It turns your entire program into a function with parameters, meaning that it is controllable from the outside. It's not as 'weak' as general input. In some ways it's still deterministic per program run, but it's strictly weaker than fully sandboxing your program and not allowing any input. Maybe we just use the self keyword as the function's name instead of main. (a)self(b) = a + b.




DISALLOWED (allowed in sepal)
ignore
ADDED
within
self

WE NEED A SECTION ON STRICT VS PROTO TYPES
overflow, saturate, ;
//static ??? not sure if static is opt in or opt out (or opt at all. maybe not part of base Trillia)
//dynamic ??? maybe Trillia is static by default, and dynamic as opt in. idk.









