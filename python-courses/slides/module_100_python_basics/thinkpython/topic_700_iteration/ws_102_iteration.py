# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 3
#
# - We will practice the concepts of iteration, which are fundamental to programming in Python
# - This workshop contains exercises that require you to use loops to solve different problems ranging from numerical computations to processing collections of data

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 1: The Power of While Loops
#
# - Write a function named `countdown` that takes an integer `n`.
# - Using a `while` loop, print from `n` down to `1`, followed by `"Liftoff!"`.
# - The function doesn't need to return anything, just print the countdown.


# %% lang="en"
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")


# %% lang="en"
# Uncomment to test your function
# countdown(5)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 2: Iterating Over Sequences
#
# - Given a list of integers `numbers`, write a function named `sum_odd_numbers` that returns the sum of all odd numbers in the list.
# - Utilize a `for` loop to iterate over the elements in the list.
# - Hint: Remember the modulo operator `%` to check if a number is odd.


# %% lang="en"
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


# %% lang="en"
# Uncomment to test your function with a list of numbers
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_odd_numbers(numbers_list))

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Exercise 3: Fibonacci Sequence
#
# - Write a function called `fibonacci` that takes an integer `n` and prints the first `n` numbers of the Fibonacci sequence.
# - The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it.
# - For example, the first 10 numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
# - Use iteration (loops) in your solution.


# %% lang="en"
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


# %% lang="en"
# Uncomment to test your function
# fibonacci(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# - Congratulations on completing the iteration workshop! These exercises aimed to strengthen your understanding of loops in Python, an essential concept for iterative problem-solving in programming.
