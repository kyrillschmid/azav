# %% [markdown] lang="en" tags=["slide"]
# ## Mini-workshop 9

# %% [markdown] lang="en" tags=["subslide"]
# Iterating Over a List
# - Given the list `num_list` containing the numbers from 1 to 5, write a `for` loop that prints each number multiplied by 2.

# %%
num_list = [1, 2, 3, 4, 5]

# %%
# Your code here
for num in num_list:
    print(num * 2)

# %% [markdown] lang="en" tags=["subslide"]
# ### Using Enumerate
#
# - Modify the previous loop to also print the index of each element before multiplying it by 2. Utilize `enumerate` in your solution.

# %%
# Your code here
for index, num in enumerate(num_list):
    print(f"Index: {index}, Number: {num*2}")

# %% [markdown] lang="en" tags=["subslide"]
# ### List Comprehension
#
# - Use a list comprehension to create a new list named `squared_list` containing the squares of all numbers in `num_list`.

# %%
# Your code here
squared_list = [num**2 for num in num_list]
squared_list

# %% [markdown] lang="en" tags=["subslide"]
# ### Iterating Over a Dictionary
#
# - Given the dictionary `colors_with_codes`, iterate over it to print each color name (key) along with its color code (value).
# - `colors_with_codes` is defined with colors as keys and their hexadecimal codes as values.

# %%
colors_with_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# %%
# Your code here
for color, code in colors_with_codes.items():
    print(f"{color}: {code}")

# %% [markdown] lang="en" tags=["subslide"]
# ### While Loop with Condition
#
# - Using a while loop, print numbers from 1 to 10. Use a variable to track the current number and increment it in each iteration.

# %%
# Your code here
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# %% [markdown] lang="en" tags=["subslide"]
# ### Break Statement
#
# - Modify the previous while loop to stop (using the `break` statement) when the current number reaches 5.

# %%
# Your code here
current_number = 1
while True:
    if current_number > 5:
        break
    print(current_number)
    current_number += 1

# %% [markdown] lang="en" tags=["subslide"]
# Congratulations for completing the iteration techniques workshop! You've practiced iterating over lists and dictionaries, using enumerate, list comprehensions, while loops, and controlling loop execution with `break`.
