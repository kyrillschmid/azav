# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-workshop 8
#
# The goals of this workshop are:
# 1. To understand and apply the `while` loop for repeated actions.
# 2. To utilize the `break` statement to exit a loop based on a dynamic condition.
# 3. To practice iterative processing of user input.
#
# Let's get started with iteration in Python!

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 1: Infinite Echo
#
# - Write a program that continuously asks the user for input and prints what the user typed.
# - The program should break the loop and stop if the user types `"quit"`.
#
# Example of expected functionality:
# ```
# > Hello
# Hello
# > How are you?
# How are you?
# > quit
# ```

# %% lang="en"
while True:
    user_input = input("> ")
    if user_input == "quit":
        break
    print(user_input)

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 2: Counting Numbers
#
# - Using a `while` loop, write a program that counts from 1 to 10 and prints each number to the console.
# - The loop should stop once it reaches 10.

# %% lang="en"
count = 1
while count <= 10:
    print(count)
    count += 1

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 3: User-Controlled Countdown
#
# - Ask the user to input a number.
# - Using a `while` loop, perform a countdown from that number to 1 on the console, and then print `"Liftoff!"`.
#
# Example of expected functionality:
# ```
# Enter a number to countdown from: 5
# 5
# 4
# 3
# 2
# 1
# Liftoff!
# ```

# %% lang="en"
number = int(input("Enter a number to countdown from: "))
while number > 0:
    print(number)
    number -= 1
print("Liftoff!")

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Task 4: Simple Interest Calculator
#
# - Prompt the user for:
#   - The principal amount (`P`)
#   - The annual interest rate (`r`) as a percentage (e.g., 5 for 5%)
#   - The time period in years (`t`)
# - Calculate the simple interest using the formula `SI = (P * r * t) / 100`
# - Print the calculated simple interest to the console rounded to two decimal places.
#
# Example of expected functionality:
# ```
# Enter the principal amount: 1000
# Enter the annual interest rate (%): 5
# Enter the time period in years: 2
# The simple interest is: 100.0
# ```

# %% lang="en"
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period in years: "))
simple_interest = (principal * interest_rate * time_period) / 100
print(f"The simple interest is: {simple_interest:.2f}")

# %% [markdown] lang="en" tags=["slide"]
# ## 7.5 Square Roots
# - Loops are vital for iteratively improving numerical results
# - Newton's method is a classic example for computing square roots
# - Starting with an estimate, we iteratively refine it to get closer to the actual square root

# %% [markdown] lang="en" tags=["slide"]
# ## Iterative Improvement
# - An initial estimate `x` is progressively improved using `y = (x + a/x) / 2`
# - This process is repeated until the estimate no longer changes significantly

# %% [code]
a = 4
x = 3
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [code]
x = y
y = (x + a / x) / 2
print(y)

# %% [markdown] lang="en" tags=["slide"]
# ## Checking for Convergence
# - Directly comparing floating-point numbers is risky due to precision issues
# - Instead, we check if the absolute difference is smaller than a tiny value `epsilon`
# - This approach guides us to stop the iteration once the estimate is precise enough

# %% [code]
epsilon = 0.0000001
while True:
    print(x)
    y = (x + a / x) / 2
    if abs(y - x) < epsilon:
        break
    x = y
