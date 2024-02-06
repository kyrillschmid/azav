# j2 from 'macros.j2' import header
# {{ header("Workshop - Ein erstes Programm", "Workshop - The first program") }}

# %% [markdown] lang="en" tags=["slide"]
#
# ## Mini-Workshop: The first program

# %% [markdown] lang="de" tags=["slide"]
# ## Mini-Workshop: Das erste Programm

# %% [markdown] lang="en" tags=["subslide"]
#
# The tradition in learning a new programming language is to start with a simple program that prints "Hello, World!" to the screen. This task helps you become familiar with the basic syntax of the language for printing text to the console.

# %% [markdown] lang="de" tags=["subslide"]
# Die Tradition beim Erlernen einer neuen Programmiersprache ist es, mit einem einfachen Programm zu beginnen, das "Hallo Welt!" auf den Bildschirm druckt. Diese Aufgabe hilft Ihnen, mit der grundlegenden Syntax der Sprache für die Ausgabe von Text in der Konsole vertraut zu werden.

# %% [markdown] lang="en" tags=["subslide"]
# Write a function called `hello_world()` that prints "Hello, World!" to the screen.

# %% [markdown] lang="de" tags=["subslide"]
# Schreiben Sie eine Funktion namens `hello_world()`, die "Hallo Welt!" auf den Bildschirm druckt.


# %%
def hello_world():
    print("Hello, World!")


# %% [markdown] lang="en" tags=["subslide"]
#
# Now, call the function `hello_world()` to print "Hello, World!".

# %% [markdown] lang="de" tags=["subslide"]
#
# Rufen Sie die Funktion `hello_world()` auf, um "Hallo Welt!" zu drucken.

# %%
hello_world()

# %% [markdown] lang="en" tags=["subslide"]
#
# ### Examining the Hello, World! program
#
# - The quotation marks define a string that is passed as an argument to the `print()` function.
# - The `print()` function displays the string on the screen.
#
# Let’s enhance our function. Modify `hello_world()` so that it takes a parameter `name` and prints "Hello, `name`!" where `name` is the value of the parameter. Provide a default value of "World" for `name`.

# %% [markdown] lang="de" tags=["subslide"]
#
# ### Untersuchung des Hallo-Welt-Programms
#
# - Die Anführungszeichen definieren eine Zeichenkette, die als Argument an die `print()`-Funktion übergeben wird.
# - Die `print()`-Funktion zeigt die Zeichenkette auf dem Bildschirm an.
#
# Lassen Sie uns unsere Funktion verbessern. Ändern Sie `hello_world()`, sodass sie einen Parameter `name` entgegennimmt und "Hallo, `name`!" ausgibt, wobei `name` der Wert des Parameters ist. Geben Sie für `name` einen Standardwert von "World" an.


# %%
def hello_world(name="World"):
    print(f"Hello, {name}!")


# %% [markdown] lang="en" tags=["subslide"]
#
# Test the enhanced `hello_world()` function by:
#
# 1. Calling it without arguments.
# 2. Calling it with your name as the argument.

# %% [markdown] lang="de" tags=["subslide"]
#
# Testen Sie die verbesserte `hello_world()`-Funktion, indem Sie:
#
# 1. Sie ohne Argumente aufrufen.
# 2. Sie mit Ihrem Namen als Argument aufrufen.

# %%
hello_world()
hello_world("Alice")

# %% [markdown] lang="en" tags=["subslide"]
#
# **Congratulations!** You’ve successfully created and modified your first Python program.
# - This exercise demonstrated the basic structure of a Python program and introduced you to the `print()` function and string manipulation. As you continue learning Python, you'll build upon these foundational concepts to create more complex and powerful programs.

# %% [markdown] lang="de" tags=["subslide"]
#
# **Herzlichen Glückwunsch!** Sie haben erfolgreich Ihr erstes Python-Programm erstellt und geändert.
# - Diese Übung hat die grundlegende Struktur eines Python-Programms gezeigt und Sie mit der `print()`-Funktion und der Zeichenkettenmanipulation vertraut gemacht. Wenn Sie weiter Python lernen, werden Sie auf diesen Grundkonzepten aufbauen, um komplexere und leistungsfähigere Programme zu erstellen.
