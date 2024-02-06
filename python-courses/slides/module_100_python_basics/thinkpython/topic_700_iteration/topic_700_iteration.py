# j2 from 'macros.j2' import header
# {{ header("Iteration", "Iteration") }}

# %% [markdown] lang="en" tags=["slide"]
# # Iteration
# - Iteration allows running a block of statements multiple times
# - Previously explored iteration types include recursion and `for` loops
# - This chapter introduces iteration via `while` loops
# - Additionally, we'll discuss more about variable assignment

# %% [markdown] lang="en" tags=["slide"]
# - Recursion is a form of iteration where a function calls itself
# - `for` loops iterate over elements of a sequence or iterable
# - `while` loops continue executing as long as a condition remains true

# %% [markdown] lang="en" tags=["slide"]
# ## Variable Assignment Revisited
# - Variable assignment is crucial in controlling the flow of iteration
# - Proper management of variable values is essential for accurate and efficient iterations
# - In the context of loops, variable assignment often involves initializing counters or accumulators before the loop starts
# - Updating variable values appropriately within the loop body is key to avoiding infinite loops or incorrect results


# %% [markdown] lang="en" tags=["slide"]
# ## Reassignment
# - Variables can be assigned multiple times; later assignments change the variable's reference
# - Initial display of `x` shows value of 5, subsequent display shows value of 7
# - Python's equal sign (`=`) means assignment, not mathematical equality
# - Reassignment can make variables temporarily equal, but they may not remain that way

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Python Assignment
# - Assignment is not a symmetric relationship like mathematical equality
#   - `a = 7` is valid, whereas `7 = a` is not
# - Assignment creates a temporary equality, not a permanent one
#   - Example: assigning `b = a` makes them equal until `a` changes
# - Use reassignment cautiously to avoid code confusion and debugging issues

# %%
x = 5
x

# %%
x = 7
x

# %%
a = 5
b = a  # a and b are now equal
a = 3  # a and b are no longer equal
b

# %% [markdown] lang="en" tags=["slide"]
# ## The while statement
# - Computers excel at automating repetitive tasks, a concept known as iteration in programming.
# - Python offers `while` and `for` statements to facilitate iteration.
# - The `while` statement is used to repeat a task while a condition is true.
# - We'll explore how to use `while` with examples, including how to avoid infinite loops.

# %% [markdown] lang="en" tags=["slide"]
# ### Countdown Example with `while`
# - A `while` loop can make the countdown process straightforward.
# - The structure of a `while` loop allows for repetitive tasks based on a condition.
# - It keeps executing its block of code as long as the condition remains true.
# - Let's look at a countdown example using a `while` loop:


# %%
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff!")


# Example usage
countdown(5)

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding `while` Loops
# - The flow of a `while` loop includes checking a condition and executing the loop body if the condition is true.
# - If the condition becomes false, the loop terminates and execution continues with the next statement.
# - To prevent infinite loops, ensure that the loop condition will eventually become false.
# - Infinite loops are a common error, akin to an endless shampoo bottle instruction: "Lather, rinse, repeat."

# %% [markdown] lang="en" tags=["slide"]
# ## Example: Sequence Generation with `while`
# - Let's explore a more complex example, where a sequence of numbers is generated until a certain condition is met.
# - This example illustrates how to deal with even and odd numbers differently in a loop.
# - The loop condition is designed to continue until a specific value is reached.
# - Understanding the termination condition for this loop can be challenging.


# %%
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else:  # n is odd
            n = n * 3 + 1


# Example usage
sequence(3)

# %% [markdown] lang="en" tags=["slide"]
# ## Loop Termination and the Collatz Conjecture
# - Determining whether certain loops terminate can sometimes be straightforward and, at other times, extremely complex.
# - The sequence example introduces the Collatz conjecture, an unsolved mathematical problem.
# - For some loops, proving termination depends on the input values and the loop's behavior.
# - The Collatz conjecture poses a challenging question: does the sequence loop terminate for all positive integers?

# %% [markdown] lang="en" tags=["slide"]
# ## The `break` Statement
# - The `break` statement is used to exit a loop prematurely
# - This is useful when you need to stop the loop based on a condition that is checked within the loop's body, rather than at the start

# %% [markdown] lang="en" tags=["slide"]
# ## Example: User Input Loop
# - When you want to keep taking input from the user until a specific input is received
# - The loop's condition is set to `True` to ensure it keeps running indefinitely
# - The `break` statement is then used to exit the loop based on the user's input

# %%
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)

print("Done!")

# %% [markdown] lang="en" tags=["slide"]
# ## Sample Run
# - In a sample run, the program keeps asking for input
# - If the user types "done", the program exits the loop and prints "Done!"
# - This illustrates the dynamic control you have within loops using the `break` statement

# %%
# Sample Input
"> not done"
"not done"
"> done"
"Done!"


# %% [markdown] lang="en" tags=["slide"]
# ## Algorithms
# - Newton's method illustrates what an algorithm is: a mechanical process for solving a certain category of problems, such as computing square roots.
# - Algorithms contrast with memorized solutions, embodying general solutions to problems rather than specific answers.
# - Examples include techniques for addition with carrying, subtraction with borrowing, and long division—all of which are algorithms.
# - A hallmark of algorithms is their mechanical nature, requiring no intelligence to execute, merely following a set of simple rules.

# %% [markdown] lang="en" tags=["slide"]
# ## Characteristics and Challenges of Algorithms
# - Designing algorithms is intriguing and central to computer science, focusing on formulating a series of steps to solve problems.
# - A key challenge in algorithm design is handling tasks that humans perform intuitively, such as understanding natural language.
# - These natural abilities, effortless for humans, are difficult to translate into algorithmic form.
# - This discrepancy highlights both the complexity of human cognition and the intellectual challenges in computer science.


# %% [markdown] lang="en" tags=["slide"]
# ## Debugging
# - Writing larger programs increases debugging time due to more code and potential error spots
# - Debugging by bisection can significantly reduce debugging time
#   - Example: Debugging 100 lines of code by bisection vs. line by line
# - Place check points in the program to narrow down the error location

# %% [markdown] lang="en" tags=["slide"]
# ## Efficient Debugging Strategies
# - Add a print statement near the mid-point of the program to verify intermediate values
# - Incorrect mid-point checks indicate problems in the first half of the program, and vice versa
# - Each check effectively halves the potential error space, streamlining error identification

# %% [markdown] lang="en" tags=["slide"]
# ## Practical Debugging Tips
# - Identifying the "middle of the program" isn't about counting lines but assessing error-prone areas
# - Strategically place checks where errors are likely or verification is simple
# - Aim to choose check points that make it equally probable for errors to be before or after the check

# %% [markdown] lang="en" tags=["slide"]
# ## Example of Debugging by Bisection
# - A practical approach to localize the error in fewer steps
# - Not always about finding the exact midpoint but about smartly dividing the problem space
# - Effective use of print statements or other verifiable actions can greatly aid in narrowing down the bug's location

# %% lang="python" tags=["code"]
# Example of adding a print statement to debug:
# Imagine having a function that is not giving the expected output


# %%
def problematic_function(x):
    # Some complex logic here...
    result = x**2 - 2 * x + 1  # An intended operation
    # More complex logic...
    return result


x_test = 4  # Test value
print("Intermediate check:", problematic_function(x_test))
# This print statement serves as a midpoint check to verify the function's behavior

# %%
# Depending on the output of the print statement, we can deduce if the error
# lies before or after this point in the overall logic of our program.


# %% [markdown] lang="en" tags=["slide"]
# ## Glossary
# - Reassignment refers to assigning a new value to an existing variable
# - Update is a specific type of assignment where the variable's new value depends on its old value

# %% [markdown] lang="en" tags=["slide"]
# - Initialization involves giving an initial value to a variable intended for future updates
# - Increment and decrement are types of updates that respectively increase or decrease the value of a variable

# %% [markdown] lang="en" tags=["slide"]
# - Iteration denotes the repeated execution of a set of statements, achieved via loops or recursive function calls
# - An infinite loop occurs when a loop's terminating condition is never met, causing endless iteration

# j2 include "ws_100_iteration.py"

# j2 include "ws_101_iteration.py"

# j2 include "ws_102_iteration.py"

# j2 include "ws_103_iteration.py"

# j2 include "ws_104_iteration.py"

# j2 include "ws_105_iteration.py"

# j2 include "ws_106_iteration.py"

# j2 include "ws_107_iteration.py"

# j2 include "ws_108_iteration.py"
