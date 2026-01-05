



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






# This is the Transpiler for Trillia.
# The Transpiler is written in Python, takes in valid Trillia code as text input, and outputs valid C code.

# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## #####      C O M P I L E R _ V A R I A B L E S      ##### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #

# This is where we initialize variables. Most are initially in the False state, and are changed later in the program for diagnosis and tracking.

    # PHASE 0: VARIABLES
variables_phase_entered           = True          # This is True if we have entered the variable phase. It remains True.
variables_phase_exited            = False         # This is True if we have exited  the variable phase. It remains True.

    # PHASE 1: INPUT
input_phase_entered               = False         # This is True if we have entered the input phase. It remains True.
trillia_input                     = ""            # This will be replaced with the actual input written in Trillia, represented as a string, later in the program.
input_phase_exited                = False         # This is True if we have exited  the input phase. It remains True.
# Phase 1 is complete

    # PHASE 2: TOKENIZATION
tokenization_phase_entered        = False         # This is True if we have entered the tokenization phase. It remains True.
juno                              = 0             # This is the primary auxiliary cursor variable
rhea                              = 0             # This is the secondary auxiliary cursor variable
trillia_line_array                = []            # This is a much less sophisticated array. It merely dipicts the Trillia code split into elements by line number. line 0 is empty, line 1 is index 1.
indentation_counter               = 0             # This variable counts how many whitespaces precede the code on each line.
trillia_spaceless_line_array      = []            # This is like the trillia_line_array, but with indentation and all spaces removed
token_array                       = [None]        # This is where trillia tokens are inserted.
tokenization_phase_exited         = False         # This is True if we have exited  the tokenization phase. It remains True.

    # PHASE 3: SYNTHESIS
synthesis_phase_entered           = False         # This is True if we have entered the synthesis phase. It remains True.
include_stdbool                   = False         # This keeps track of whether stdbool needs to be included.
include_stdlib                    = False         # This keeps track of whether stdlib  needs to be included.
include_stdint                    = False         # This keeps track of whether stdind  needs to be included.
include_string                    = False         # This keeps track of whether string  needs to be included.
include_limits                    = False         # This keeps track of whether limits  needs to be included.
include_stdio                     = False         # This keeps track of whether stdio   needs to be included.
include_math                      = False         # This keeps track of whether math    needs to be included.
include_time                      = False         # This keeps track of whether time    needs to be included.
synthesis_phase_exited            = False         # This is True if we have exited  the synthesis phase. It remains True.


# custom functions used for the compiler:
def rcolor():
    print("\x1b[31m", end="")

def wcolor():
    print("\x1b[39m", end="")


variables_phase_exited            = True

# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## #####             I N P U T _ P H A S E             ##### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #

input_phase_entered = True

# Put your Trillia code in here in the form of a string.
# The format should be such that the actual code starts on the line after the 'trillia_input' definition line.
# The format should be such that also the end quotes are on the line after the last line of Trillia code.
trillia_input = """
int32 x = 6
c_printf("%d", x)
"""

input_phase_exited = True

# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## #####      T O K E N I Z A T I O N _ P H A S E      ##### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #






# INDENT and DEDENT should exist

tokenization_phase_entered = True

# This splits the Trillia program by line number. Instrumental for crash logging.
trillia_line_array = trillia_input.split("\n")
while trillia_line_array[-1] == "": # This shaves off any unneeded empty lines of code at the end.
    trillia_line_array.pop()
trillia_line_array[0] = None # This is just to ensure that I know this is supposed to be empty. There is no "line 0"
print(trillia_line_array)

# This ensures that we don't go out of range by ensuring that trillia_line_array and token_array are the same length
while len(token_array) < len(trillia_line_array):
    token_array.append([])


# This goes through all indentation, and appends \t tokens into the token array.
juno = 1
rhea = 0
while juno < len(trillia_line_array):
    while rhea < len(trillia_line_array[juno]):
        if trillia_line_array[juno][rhea] == " ":
            indentation_counter += 1
            rhea += 1
        else:
            if indentation_counter % 4 == 0:
                while indentation_counter > 0:
                    indentation_counter -= 4
                    token_array[juno].append("INDENT")
            else:
                rcolor(), print("INDENTATION_ERROR: on line", juno, "at position", rhea, "Expected spacing is a multiple of 4"), wcolor() # We need a way to actually halt the program
                quit() # We crash the compiler
            juno += 1
            rhea = 0
            if juno >= len(trillia_line_array):
                break

# This ensures that we have empty array boxes to append tokens into
juno = 0
while juno < len(trillia_line_array):
    trillia_spaceless_line_array.append([])
    juno += 1
trillia_spaceless_line_array[0] = None

# This ensures that those boxes are filled with a version of trillia line array that is split at the space separator.
juno = 1
while juno < len(trillia_line_array):
    trillia_spaceless_line_array[juno] = trillia_line_array[juno].split(" ")
    juno += 1

# This ensures that spaces are used as separators, and ignored beyond that.
# Do note that this is not perfect. This function does not split off prefixes, suffixes, grammar symbols, or brackets
juno = 1
rhea = 0
while juno < len(trillia_spaceless_line_array):
    while rhea < len(trillia_spaceless_line_array[juno]):
        if trillia_spaceless_line_array[juno][rhea] == "":
            trillia_spaceless_line_array[juno].pop(rhea)
        else:
            rhea += 1
    else:
        rhea = 0
        juno += 1


# We definitely want to make the inserted symbols be INDENT and DEDENT
# 1 - everything split by new-line characters
# 2 - every line split by spaces
# 3 - INDENT and DEDENT


print(trillia_spaceless_line_array)

print(token_array)

c_token_array = trillia_spaceless_line_array

debug = False




# We get rid of anything that isn't a line of code.
if c_token_array.count(None) > 0:
    c_token_array.remove(None)



# juno is an index
# rhea is the object itself

for juno in range(0, len(c_token_array)):
    if isinstance(c_token_array[juno], list):
        for rhea in c_token_array[juno]:
            if rhea == "int32": ## I DIDN'T THINK THIS FAR AHEAD
                pass





print(c_token_array)
print(debug)


# 1: we split the program by new line characters. This is good for error handling.
#COMPLETE

# 2: we take put \t in the token array
# 3: we get rid of tabs from the trillia_line_array, optionally making a new array instead that holds the tabless form "trillia_tabless_line_array"
# 4: we split the remaining tokens by whitespace and get rid of all whitespace characters in the no_whitespace array.
# 5: we determine where there ought to be suffix or prefix tokens, or whether there is a crash based on incorrectly placed tokens.





tokenization_phase_exited = True

# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## #####         S Y N T H E S I S _ P H A S E         ##### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #
# ## ##### ########## ######################################################### ########## ##### ## #

synthesis_phase_entered = True

# These are all of the Include statements. They are inserted conditionally based on whether or not they are needed.
if include_stdbool == True:
    print("#include <stdbool.h>")   # This allows you to use booleans
if include_stdlib  == True:
    print("#include  <stdlib.h>")   # This allows you to do many things such as random()
if include_stdint  == True:
    print("#include  <stdint.h>")   # This allows fixed-sized integers  int32 x = 99          -> int32_t x = 99;
if include_string  == True:
    print("#include  <string.h>")   # This allows string manipulation
if include_limits  == True:
    print("#include  <limits.h>")   # This allows for specific size limits on variables int60 instead of int64
if include_stdio   == True:
    print("#include   <stdio.h>")   # This allows you to print          printf("hello world") -> printf("hello world");
if include_math    == True:
    print("#include    <math.h>")   # This allows pow()
if include_time    == True:
    print("#include    <time.h>")   # This allows date and time
if include_stdbool == True or include_stdlib == True or include_stdint == True or include_string == True or include_limits == True or include_stdio == True or include_math == True or include_time == True:
    print("")                       # this creates a new line to exist as space between the include statements and the rest of the code.

# This is the main function
print("int main() {")

################################################
### The actual code that you write goes here ###
################################################
print("") # newline


# This is the end bracket for the main function
print("return 0;\n}\n")

synthesis_phase_exited = True













































"""
#include <stdio.h>
int main() {
void collatz() {
    int    x = 1;
    int juno = 1;
    while (1) {
        printf("%d\n", juno);
        if (juno == 1) {
            x += 1;
            juno = x;
        } else if (juno % 2 == 0) {
            juno /= 2;
        } else {
            juno = juno * 3 + 1;
        }
    }
}
collatz();
return 0;
}
"""

"""
#include <stdio.h>
int main() {
void collatz() {
    _BitInt(64) x = 1;
    _BitInt(64) juno = 1;
    while (1) {
        printf("%d\n", juno);
        if (juno == 1) {
            x += 1;
            juno = x;
        } else if (juno % 2 == 0) {
            juno /= 2;
        } else {
            juno = juno * 3 + 1;
        }
    }
}
collatz();
return 0;
}










collatz() =
    x, juno = 1
    repeat
        print(juno)
        if juno = 1
            x + 1
            juno = x
        else if juno /@ 2
            juno / 2
        else
            juno * 3 + 1
collatz()




#INT64 VERSION. BETTER FOR CONVERSION TO C
collatz() =
    int64 x = 1
    int64 juno = 1
    repeat
        printn(juno)
        if juno = 1
            x + 1
            juno = x
        else if juno /@ 2
            juno / 2
        else
            juno * 3 + 1
collatz()


Tokens
[FN_collatz, L_BRACK, R_BRACK, FN=]
[INDENT, INT64, VAR_x, =, 1]
[INT64, VAR_juno, =, 1]
[REPEAT]
[INDENT, FN_printn, L_BRACK, VAR_juno, R_BRACK]
[IF, VAR_juno, ?=, 1]
[INDENT, VAR_x, REL+, 1]
[VAR_juno, =, x]
[DEDENT, ELSE, IF, VAR_juno, /@, 2]
[INDENT, VAR_juno, REL/, 2]
[DEDENT, ELSE]
[INDENT, RELASS VAR_juno, *, 3, +, 1] -> [INDENT, VAR_juno, REL*, 3] [RELASS VAR_juno, REL+, 1]
[DEDENT, DEDENT, DEDENT, FN_collatz, L_BRACK, R_BRACK]





TOKENS
FN_collatz L_BRACK R_BRACK ASSIGN ;
INDENT INT64 VAR_x ASSIGN 1 ;
INT64 VAR_juno ASSIGN 1 ;
REPEAT ;
INDENT FN_printn L_BRACK VAR_juno R_BRACK ;
IF VAR_juno ASSIGN 1 ;
INDENT VAR_x REL_ADD 1 ;
VAR_juno ASSIGN VAR_x ;
DEDENT ELSE IF VAR_juno DIVIDE_AT 2 ;
INDENT VAR_juno REL_DIVIDE 2 ;
DEDENT ELSE ;
INDENT VAR_juno REL_MULTIPLY 3 REL_ADD 1 ;
DEDENT_ALL FN_collatz L_BRACK R_BRACK ;







"""


"""
[
["\n", "t_collatz", "(", ")", "="],
["\n", "\t", "t_x", "=", "1"],
["\n", "\t", "t_juno", "=", "1"],
["\n", "\t", "repeat"],
["\n", "\t", "\t", "print", "(", "t_juno", ")"],
["\n", "\t", "\t", "if", "t_juno", "=", "1"],
["\n", "\t", "\t", "\t", "t_x", "+", "1"],
["\n", "\t", "\t", "\t", "t_juno", "=", "t_x"],
["\n", "\t", "\t", "else", "if", "t_juno", "/@", "2"],
["\n", "\t", "\t", "\t", "t_juno", "/", "2"],
["\n", "\t", "\t", "else"],
["\n", "\t", "\t", "\t", "t_juno", "*", "3", "+", "1"],
["\n", "t_collatz", "(", ")"]
]







int32 x = 6
    c_printf("%d", x)

_BitInt(32) x = 6;
printf("%d", x);



"""




