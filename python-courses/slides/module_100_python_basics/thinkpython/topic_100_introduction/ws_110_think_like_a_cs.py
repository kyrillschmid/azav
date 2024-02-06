# j2 from 'macros.j2' import header
# {{ header("Workshop - Denken wie ein Informatiker", "Workshop - Thinking like a Computer Scientist") }}

# %% [markdown] lang="en" tags=["slide"]
#
# ## Mini-Workshop: Introduction to Programming

# %% [markdown] lang="de" tags=["slide"]
# ## Mini-Workshop: Einführung in die Programmierung

# %% [markdown] lang="en"
#
# The goal of this mini-workshop is to introduce you to the idea of thinking like a computer scientist, which involves understanding how to approach problem solving in a systematic and logical manner. We'll start with a basic exercise that gives you a taste of programming and problem-solving.

# %% [markdown] lang="de"
# Das Ziel dieses Mini-Workshops ist es, Sie mit der Idee vertraut zu machen, wie ein Informatiker zu denken, was das Verständnis beinhaltet, wie man Problemlösungen auf systematische und logische Weise angeht. Wir werden mit einer grundlegenden Übung beginnen, die Ihnen einen Einblick in das Programmieren und Problemlösen gibt.

# %% [markdown] lang="en" tags=["slide"]
#
# Write a function `greet(name)` that prints a greeting to the screen. The function should take a string `name` as an argument and print the message `"Hello, {name}! Welcome to the world of Python!"`.


# %% [markdown] lang="de" tags=["slide"]
# Schreibe eine Funktion `greet(name)`, die eine Begrüßung auf dem Bildschirm ausgibt. Die Funktion sollte einen String `name` als Argument entgegennehmen und die Nachricht `"Hallo, {name}! Willkommen in der Welt von Python!"` ausgeben.


# %%
def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python!")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test the function `greet(name)` with your name and observe the output.

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie die Funktion 'grüße(name)' mit Ihrem Namen und beobachten Sie die Ausgabe.

# %%
greet("Alice")

# %% [markdown] lang="en" tags=["subslide"]
#
# Problem solving involves breaking down a problem into smaller, more manageable parts and then solving each part. Let's practice this by writing a function `is_positive(number)` that:
#
# - Returns `True` if `number` is positive.
# - Otherwise, returns `False`.


# %% [markdown] lang="de" tags=["subslide"]
# ## Problem lösen
# Problemlösung beinhaltet, ein Problem in kleinere, leichter zu bewältigende Teile zu zerlegen und dann jeden Teil zu lösen. Üben wir dies, indem wir eine Funktion `is_positive(number)` schreiben, die:
# - `True` zurückgibt, wenn `number` positiv ist.
# - Ansonsten `False` zurückgibt.


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


# %%
def is_positive(number):
    return number > 0


# %% [markdown] lang="en" tags=["subslide"]
#
# Write assertions to test the `is_positive()` function to ensure it returns correct results for -1, 0, and 5.

# %% [markdown] lang="de" tags=["subslide"]
# Schreiben Sie Behauptungen, um die Funktion 'is_positive()' zu testen, um sicherzustellen, dass sie korrekte Ergebnisse für -1, 0 und 5 zurückgibt.

# %%
assert not is_positive(-1)
assert not is_positive(0)
assert is_positive(5)

# %% [markdown] lang="en" tags=["subslide"]
#
# By writing these small functions and testing them, you are practicing the problem-solving approach of breaking problems down and verifying solutions at each step.
#
# Next, write a function `describe_number(number)` that:
#
# - Prints "`number` is positive." if the number is positive.
# - Prints "`number` is zero." if the number is 0.
# - Prints "`number` is negative." if the number is negative.
#
# Use the `is_positive()` function as part of your solution.


# %% [markdown] lang="de" tags=["subslide"]
# Durch das Schreiben dieser kleinen Funktionen und deren Testen üben Sie den problemorientierten Ansatz, Probleme zu zerlegen und Lösungen in jedem Schritt zu überprüfen.

# Als Nächstes schreiben Sie eine Funktion `describe_number(number)`, die:

# - Ausgibt "`number` ist positiv." wenn die Zahl positiv ist.
# - Ausgibt "`number` ist null." wenn die Zahl 0 ist.
# - Ausgibt "`number` ist negativ." wenn die Zahl negativ ist.

# Verwenden Sie die Funktion `is_positive()` als Teil Ihrer Lösung.


# %%
def describe_number(number):
    if is_positive(number):
        print(f"{number} is positive.")
    elif number == 0:
        print(f"{number} is zero.")
    else:
        print(f"{number} is negative.")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test `describe_number(number)` with the values -5, 0, and 10.

# %% [markdown] lang="de" tags=["subslide"]
# Testen Sie `describe_number(zahl)` mit den Werten -5, 0 und 10.

# %%
describe_number(-5)
describe_number(0)
describe_number(10)

# %% [markdown] lang="en" tags=["subslide"]
#
# Congratulations! You've taken your first steps into the world of programming by learning to think like a computer scientist and practicing problem-solving. Remember, the key is to break down problems into smaller parts, solve each part, and then combine the solutions. Continue practicing these skills, and you'll become more proficient over time.
# %% [markdown] lang="de" tags=["subslide"]
# Glückwunsch! Sie haben Ihre ersten Schritte in die Welt des Programmierens gemacht, indem Sie gelernt haben, wie ein Informatiker zu denken und Problemlösung zu üben. Denken Sie daran, dass es wichtig ist, Probleme in kleinere Teile zu zerlegen, jeden Teil zu lösen und dann die Lösungen zu kombinieren. Üben Sie diese Fähigkeiten weiterhin, und mit der Zeit werden Sie immer versierter werden.
