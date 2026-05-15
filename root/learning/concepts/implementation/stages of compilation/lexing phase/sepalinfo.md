This is the first phase of the Trillia compiler.

The first step of this phase is that the compiler makes a copy of your code and compresses it losslessly.
This is so that your compiled executable comes with the exact source code that compiled it.
This takes up some extra space in the binary executable files, but in exchange, you gain the ability to edit and recompile binary files losslessly.
This feature is on by default, but can be opted out.

Next, the compiler lexes the code, turning it into an interpretable intermediary representation (IR)





