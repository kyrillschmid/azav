# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 4
#
# - In this workshop, we will delve into the use of `while` loops for iteration in Python.
# - We will also reinforce our understanding of iteration with variable assignment, crucial for managing loop execution and updates efficiently.
#
# ### Task 1: Counting Up
# - Initialize a variable `counter` with the value `0`.
# - Use a `while` loop to increment `counter` by `1` until it reaches `10`.
# - Print the value of `counter` after the loop ends to confirm it's `10`.

# %% lang="en"
counter = 0
while counter < 10:
    counter += 1
print(counter)  # Should print 10

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Collecting Squares
#
# - Create an empty list named `squares`.
# - Using a `while` loop, populate this list with the squares of the numbers from `1` to `5`.
# - Ensure you use a variable to track the current number inside your loop.
# - After the loop, print `squares` to ensure it contains `[1, 4, 9, 16, 25]`.

# %% lang="en"
squares = []
number = 1
while number <= 5:
    squares.append(number**2)
    number += 1
print(squares)  # Should print [1, 4, 9, 16, 25]

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Using `while` for Input Validation
#
# - Write a `while` loop that continually prompts the user to enter their age.
# - The loop should only break if the user enters a valid age (integer from `0` to `120`).
# - After the loop ends, print a message saying `"Age entered: <age>."` with `<age>` replaced by the user's input.
# - **Hint:** Use `input()` to prompt for user input and `int()` to convert the input string to an integer. Be aware of exceptions that can occur with `int()` and handle them gracefully.

# %% lang="en"
while True:
    user_input = input("Please enter your age (0-120): ")
    try:
        age = int(user_input)
        if 0 <= age <= 120:
            break
    except ValueError:
        pass  # Ignore invalid integer inputs
print(f"Age entered: {age}.")

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Challenge Task: Fibonacci Sequence
#
# - The Fibonacci sequence is a sequence of numbers where the next number is found by adding up the two numbers before it.
# - Starting with `0` and `1`, the sequence goes `0, 1, 1, 2, 3, 5, 8, ...`
# - Using a `while` loop, generate the first `10` Fibonacci numbers and store them in a list named `fibonacci`.
# - Print `fibonacci` after the loop to ensure it contains the correct sequence.

# %% lang="en"
fibonacci = [0, 1]
while len(fibonacci) < 10:
    # Append the sum of the last two elements in the sequence
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)  # Should print the first 10 Fibonacci numbers

# %% [markdown] lang="en" tags=["slide"]
# ## 7.2  Updating Variables
# - Variable updates involve reassignment where the new value relies on its previous value.
# - Example of increment: `x = x + 1`. This pattern adds one to the current value of `x`.
# - Attempting to update a non-initialized variable results in an error: `NameError: name 'x' is not defined`.
# - Initialization before updating is crucial: `x = 0` followed by `x = x + 1`.
# - Increment (`x = x + 1`) and decrement (`x = x - 1`) are common update operations.

# %%
x = 0

# %%
x = x + 1
