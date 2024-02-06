# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 6
#

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Sum of Numbers
#
# - Create a list `numbers` containing the first ten positive integers.
# - Using a `for` loop, calculate the sum of all numbers in the `numbers` list and print the result.

# %% lang="en"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print(sum_of_numbers)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Find the Even Numbers
#
# - Given the list `numbers` from the previous task, use a `for` loop and a conditional statement to find all the even numbers in the list.
# - Append the even numbers to a new list called `even_numbers` and print it.

# %% lang="en"
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Build a Number Triangle
#
# - Using a `for` loop, print the following pattern:
# ```
# 1
# 22
# 333
# 4444
# 55555
# ```
# - Note: The pattern should be easily adjustable to accommodate more lines.

# %% lang="en"
for i in range(1, 6):
    print(str(i) * i)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: Fibonacci Sequence
#
# - The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# - Write a `for` loop to generate the first 10 numbers of the Fibonacci sequence and store them in a list called `fibonacci`.
# - The list should start with `[0, 1, 1, 2, 3, 5, ...]`.

# %% lang="en"
fibonacci = [0, 1]
for i in range(2, 10):
    next_number = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_number)
print(fibonacci)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 5: Using `while` Loops
#
# - Write a `while` loop that starts with `x = 0` and increments `x` by `1` on each iteration, printing the value of `x`.
# - The loop should terminate once `x` reaches `5`.
# - Pay careful attention to avoid creating an infinite loop.

# %% lang="en"
x = 0
while x <= 5:
    print(x)
    x += 1
