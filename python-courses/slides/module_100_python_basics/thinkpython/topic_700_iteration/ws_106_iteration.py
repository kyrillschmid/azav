# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 7
#
# Iteration is a core concept in programming, allowing repetitive execution of code blocks based on a condition. In this workshop, we'll explore the `while` loop in Python, which is a fundamental way to implement iteration.

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Simple Countdown
# - Implement a function named `simple_countdown` that takes an integer `n` and prints numbers from `n` down to `1`. After printing `1`, it should print `Go!`.
# - Use a `while` loop to implement this function.
# - Ensure that your function prints each number on a new line.


# %% lang="en"
def simple_countdown(n):
    # Your code here
    while n > 0:
        print(n)
        n -= 1
    print("Go!")


# Example usage
simple_countdown(3)


# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Oddities and Evenness
# - Implement a function named `odd_even_countdown` that takes an integer `n`.
# - If `n` is odd, it counts down only the odd numbers till 1. If `n` is even, it counts down only the even numbers till 2.
# - Use a `while` loop to implement this functionality.
# - Hint: The termination condition of the loop changes based on whether `n` is even or odd.


# %% lang="en"
def odd_even_countdown(n):
    # Your code here
    while n > 0:
        print(n)
        n -= 2 if n % 2 == 0 else 1


# Example usage
odd_even_countdown(5)  # It should print: 5, 3, 1
odd_even_countdown(6)  # It should print: 6, 4, 2

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: Accumulating Sum
# - Implement a function named `accumulating_sum` that uses a `while` loop to add numbers from 1 to `n`, inclusive.
# - The function should return the total sum after adding numbers from 1 to `n`.
# - This task helps understand how loops can be used for cumulative operations.


# %% lang="en"
def accumulating_sum(n):
    # Your code here
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


# Example usage
print(accumulating_sum(10))  # Should print 55 as the result

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: The Power of While
# - Challenge: Implement a function named `power_of_while` that takes two integers, `base` and `exponent`.
# - The function calculates `base` to the power of `exponent` using a `while` loop (i.e., `base` ** `exponent`), without using the `**` operator or `pow()` function.
# - Return the calculated value.
# - This task will help you understand how to implement mathematical operations using loops.


# %% lang="en"
def power_of_while(base, exponent):
    # Your code here
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result


# Example usage
print(power_of_while(2, 3))  # Should print 8 as the result
