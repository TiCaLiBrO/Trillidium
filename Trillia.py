



# the trillia compiler should be entirely thought out before working on it:


"""
first, you write your code

TRILLIA TO IR
initial safety checks ::
    1:    no object use before definition
    2:    make sure there are no unused objects

dependency tagging ::
    1: ownership ordering
    2: determinism endpoints (mark where an object loses determinism under a foreign function) and determinism parallelized requirement tagging
    3: ordering parallelism
    4: safety check: error if there are any dependency cycles

presolve phase ::
    1: go through each deterministic operation and solve it in parallel, returning the results back into the IR
    2: safety check: compilation error if presolve runs into an error

free insertion phase ::
    1: insert frees for any remaining object directly after their last ownership in the program if they are not static

convert everything to C ::

C and beyond ::
    macro phase
    execution (whenever you want)


at the very end, you run your code


To IR
initial safety checks
dependency tagging, reordering, parallelizing, ownership chains
presolve phase
free insertion
To C


"""










