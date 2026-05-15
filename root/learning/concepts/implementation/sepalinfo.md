Trillia's execution is very heavily dependent on which implementation of Trillia you are using.
Anyone is allowed to make their own Trillia compiler or Trillia interpreter.
In fact, I even encourage it as it helps diversify the target languages and means of executing Trillia.

Trillia can be interpreted, compiled ahead of time, or compiled just in time.
An implementation of Trillia does not need to be implemented under a specific execution method, and it is also not defined by optimizations.
A given implementation of Trillia could be thousands of times slower than another, and they are both equally Trillia.
What defines an implementation of Trillia as being a valid one depends solely on the output, not on how it reaches the output.

There may not be a single correct way to implement Trillia, but there is a theoretically optimal way, and that way is described within the manual.

The fastest possible model is an ahead-of-time compiler.
This is the default implementation unless specified otherwise.
[Stages of Compilation]()

[Orphaned Threads]()

[Complexity Classes]()







