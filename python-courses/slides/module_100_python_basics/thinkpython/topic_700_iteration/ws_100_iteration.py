# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop 1
#
# ### Introduction to Iteration with For Loops

# %% [markdown] lang="en" tags=["slide"]
# - Iteration allows you to run a block of code repeatedly with some parameters updated each time through the loop.
# - A `for` loop in Python iterates over the items of any sequence (a list, a tuple, a dictionary, a set, or a string), in the order that they appear in the sequence.
# - Let's experiment with some basic `for` loops in Python.

# %% [markdown] lang="en" tags=["subslide"]
#
#  **Simple For Loop**
#
# Use a `for` loop to print each character in the string `"Python"`.

# %% lang="en"
for character in "Python":
    print(character)

# %% [markdown] lang="en" tags=["subslide"]
#
#  **Iterating Over a List**
#
# Create a list called `fruits` with the elements `"apple"`, `"banana"`, and `"cherry"`.
# Then use a `for` loop to print each element of the list.

# %% lang="en"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# %% [markdown] lang="en" tags=["subslide"]
#
#  **Using `range()` Function**
#
# The `range()` function returns a sequence of numbers and is commonly used in `for` loops.
#
# Use a `for` loop and the `range()` function to print numbers from 1 to 5.

# %% lang="en"
for number in range(1, 6):
    print(number)

# %% [markdown] lang="en" tags=["subslide"]
#
# **Nested For Loops**
#
# Using nested `for` loops, print a 3x3 grid of asterisks (`*`).
# Your output should look like this:
#
# ```
# * * *
# * * *
# * * *
# ```

# %% lang="en"
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # to move to the next line after each row

# %% [markdown] lang="en" tags=["subslide"]
#
#  **For Loop With Else**
#
# A `for` loop can have an optional `else` block which is executed when the loop is exhausted.
# Print numbers from 1 to 3 using a `for` loop and add an `else` statement to print `"Done!"` when the loop is finished.

# %% lang="en"
for number in range(1, 4):
    print(number)
else:
    print("Done!")

# %% [markdown] lang="en" tags=["subslide"]
#
#  **Creating a Dictionary from Lists**
#
# Given two lists: `keys = ["One", "Two", "Three"]` and `values = [1, 2, 3]`, use a `for` loop to create a dictionary that maps each key to its corresponding value. Print the created dictionary.

# %% lang="en"
keys = ["One", "Two", "Three"]
values = [1, 2, 3]
mapped_dict = {}
for i in range(len(keys)):
    mapped_dict[keys[i]] = values[i]

print(mapped_dict)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Summary
# - In this workshop, we explored the basics of iteration in Python using `for` loops. We practiced iterating over strings, lists, and using functions like `range()` to generate sequences of numbers.
# - We also looked at nested loops, `for` loops with `else`, and an exercise on creating dictionaries from lists using loops.
