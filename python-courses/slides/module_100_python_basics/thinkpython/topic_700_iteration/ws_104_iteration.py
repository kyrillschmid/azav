# %% [markdown] lang="en" tags=["subslide"]
# ## Mini-workshop 5
#
# In this workshop, you will practice writing different types of loops.

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 1: Counting with Loops
#
# Use a `for` loop to count from 1 to 10, printing out each number on a new line.

# %% lang="en"
for i in range(1, 11):
    print(i)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 2: Summing Numbers
#
# Write a loop that sums all numbers from 1 to 100. Print the result.

# %% lang="en"
total = 0
for i in range(1, 101):
    total += i
print(total)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 3: Finding the Square Root
#
# - Let's manually compute the square root of a number using iteration (Newton's method shown in the examples).
# - Start with an initial guess `x` for the square root of `a = 25`, then iteratively improve the guess using the formula `y = (x + a / x) / 2`.
# - Repeat this process until the absolute difference between `y` and `x` is less than `epsilon = 0.000001`. Print each guess.

# %% lang="en"
a = 25
x = 3
epsilon = 0.000001
while True:
    y = (x + a / x) / 2
    if abs(y - x) < epsilon:
        break
    x = y
    print(x)

# %% [markdown] lang="en" tags=["subslide"]
# ### Task 4: Iterating Over Lists
#
# Given the list `items = ["apple", "banana", "cherry"]`, write a loop that iterates over the list and prints each item.

# %% lang="en"
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# %% [markdown] lang="en" tags=["subslide"]
# Congratulations on completing this mini-workshop on iteration!
# - Through these exercises, you've practiced using `for` and `while` loops for counting, summing numbers, computing square roots using an iterative method, and iterating over list items.
