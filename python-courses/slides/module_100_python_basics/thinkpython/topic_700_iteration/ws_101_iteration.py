# %% [markdown] lang="en" tags=["slide"]
# ## Mini-workshop 2
# - Define a variable `seasons` containing a list of the strings `"Spring"`, `"Summer"`, `"Autumn"`, and `"Winter"`.
# - Using a loop, print each element of the `seasons` list.

# %%
seasons = ["Spring", "Summer", "Autumn", "Winter"]

# %%
for season in seasons:
    print(season)

# %% [markdown] lang="en" tags=["subslide"]
# - Create a variable `countdown` containing the numbers from 10 down to 1 (inclusive).
# - Using a loop, print each number, followed by the word "Liftoff!" after printing the number 1.

# %%
countdown = list(range(10, 0, -1))

for number in countdown:
    print(number)
    if number == 1:
        print("Liftoff!")

### Infinite Wisdom
# - **WARNING:** This is a theoretical task. Do not run the code, as it will create an infinite loop.
# - Write a theoretical loop that would print `"Learning is endless"` indefinitely.
# ```python
# WARNING: DO NOT RUN THIS CODE
# while True:
#    print("Learning is endless")
# ```

# %% [markdown] lang="en" tags=["subslide"]
#  **Numbers and Their Squares**
# - Create a list `numbers` containing the numbers 1 through 5.
# - Using a loop, print each number and its square, formatted like: `Number: 1, Square: 1`.

# %%
numbers = list(range(1, 6))

# %%
for number in numbers:
    print(f"Number: {number}, Square: {number**2}")


# %% [markdown] lang="en" tags=["subslide"]
#  **Breaking the Loop**
# - Write a loop that prints numbers from 1 to 10 but stops (breaks) when it reaches 5.

# %%
for i in range(1, 11):
    if i > 5:
        break
    print(i)

# %% [markdown] lang="en" tags=["subslide"]
# Continue to Skip
# - Write a loop that prints numbers from 1 to 10 but skips printing the number 5.

# %%
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# %% [markdown] lang="en" tags=["subslide"]
# **Challenge: Prime Number Check**
# - Define a variable `num` with a positive integer value.
# - Write a loop to check if `num` is a prime number and print `"Prime"` if it is, or `"Not prime"` if it isn't. (Hint: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.)

# %%
num = 11  # Try different numbers
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")

# %% [markdown] lang="en" tags=["slide"]
#  **Exercises on Iteration**
# - We will cover three exercises that encapsulate the concepts of iteration
# - These exercises range from creating functions, evaluating expressions to approximating mathematical constants
# - The focus will be on developing functions for square root approximation, evaluating expressions, and approximating π
# - We aim to enhance understanding of loops, function encapsulation, and the `eval` function

# %% [markdown] lang="en" tags=["slide"]
#  **Exercise 1**: Square Root Approximation**
# - Develop a function `mysqrt(a)` that estimates the square root of `a`
# - Choose an initial guess for `x` within the function
# - Use the technique from Section 7.5 for approximation
# - Test your function with `test_square_root` to compare against `math.sqrt(a)`
# - Your test should print a table showing `a`, `mysqrt(a)`, `math.sqrt(a)`, and the difference


# %%
def mysqrt(a):
    x = a / 2  # Initial guess for the square root
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


# %%
def test_square_root(start=1, end=10):
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    for a in range(start, end + 1):
        mysqrt_a = mysqrt(a)
        math_sqrt_a = math.sqrt(a)
        diff = abs(mysqrt_a - math_sqrt_a)
        print(f"{a:.1f} {mysqrt_a:<13} {math_sqrt_a:<13} {diff}")


# %%
import math

# %%
test_square_root()

# %% [markdown] lang="en" tags=["slide"]
# **Exercise 2**: Evaluating Expressions with `eval`
# - Create a function `eval_loop` that interactively prompts the user
# - It evaluates user input with `eval` and prints the result
# - The loop ends when the user enters 'done', returning the last evaluated expression
# - This exercise demonstrates the use of `eval` for dynamic expression evaluation


# %%
def eval_loop():
    last_result = None
    while True:
        user_input = input("Enter an expression (or 'done' to exit): ")
        if user_input == "done":
            return last_result
        last_result = eval(user_input)
        print(last_result)


# %%
# Uncomment the following line to test eval_loop, but note that interactive input doesn't work well in Jupyter notebooks directly.
# eval_loop()

# %% [markdown] lang="en" tags=["slide"]
#  **Exercise 3**: Approximating π with Ramanujan's Formula
# - Implement `estimate_pi` to approximate π using Ramanujan's infinite series
# - Continue adding terms until the last term is less than `1e-15`
# - Compare your approximation with `math.pi`
# - This exercise emphasizes looping for summing a series and the use of conditional loops to achieve precision


# %%
def estimate_pi():
    import math

    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = math.factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term
        if abs(term) < 1e-15:  # Break the loop if the term is less than 1e-15
            break
        k += 1
    return 1 / total


# %%
print(f"Estimated π: {estimate_pi()}")
print(f"math.pi: {math.pi}")

# %% [markdown] lang="en" tags=["slide"]
# Using the template and structure provided in the example, let's create an iteration-focused workshop for a section in a Jupyter notebook.
