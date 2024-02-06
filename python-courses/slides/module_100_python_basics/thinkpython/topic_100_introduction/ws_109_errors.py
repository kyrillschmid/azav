# j2 from 'macros.j2' import header
# {{ header("Workshop - Fehler in Python", "Workshop - Errors in Python") }}

# %% [markdown] lang="en" tags=["subslide"]
#
# ## Mini-Workshop: Introduction to Python Errors

# %% [markdown] lang="de" tags=["subslide"]
# ## Mini-Workshop: Einführung in Python-Fehler

# Willkommen zum Mini-Workshop über Python-Fehler! In diesem Workshop werden wir verschiedene Arten von Fehlern untersuchen, die in Python auftreten können und wie man sie beheben kann.

# ### 1. Syntaxfehler
# - Syntaxfehler treten auf, wenn der Code nicht gemäß den Regeln der Programmiersprache geschrieben ist.
# - Diese Fehler werden angezeigt, wenn Sie versuchen, den Code auszuführen.
# - Beispiele für Syntaxfehler sind das Fehlen von Doppelpunkten am Ende einer Funktion oder das Vergessen von Anführungszeichen für Zeichenfolgen.

# ### 2. Ausnahmefehler (Exceptions)
# - Ausnahmefehler treten während der Ausführung des Programms auf und unterbrechen den normalen Ablauf.
# - Diese Fehler können durch try-except-Blöcke behandelt werden, um das Programm am Absturz zu hindern.
# - Beispiele für Ausnahmefehler sind Division durch Null oder das Ansprechen eines nicht vorhandenen Elements in einer Liste.

# ### 3. Logische Fehler
# - Logische Fehler treten auf, wenn das Programm kompiliert und ausgeführt werden kann, aber das Ergebnis nicht dem gewünschten Ergebnis entspricht.
# - Diese Fehler sind schwieriger zu finden, da sie nicht zu einer Fehlermeldung führen.
# - Logische Fehler erfordern gründliches Testen und Debuggen, um sie zu identifizieren und zu beheben.

# Jetzt sind Sie bereit, mehr über Python-Fehler zu lernen und wie Sie sie effektiv behandeln können!

# %% [markdown] lang="en"
#
# As part of this exercise, we'll explore common syntax errors in Python and learn to interpret and fix them. Let's start with experimenting with `print` function errors.

# %% [markdown] lang="de"
# Im Rahmen dieser Übung werden wir häufige Syntaxfehler in Python erkunden und lernen, diese zu interpretieren und zu beheben. Fangen wir damit an, Fehler bei der Verwendung der `print`-Funktion zu experimentieren.

# %% [markdown] lang="en"
# **Exercise 1**: In the following cell, intentionally make mistakes with the `print` function calls as described below. Observe and note down the errors you get:
# - Leave out one of the quotation marks in a string.
# - Leave out both quotation marks in a string.
# - Misspell the word `print`.
# - Leave out one of the parentheses, or both.

# %% [markdown] lang="de"
# **Übung 1**: Machen Sie absichtlich Fehler bei den Aufrufen der `print`-Funktion in der folgenden Zelle wie unten beschrieben. Beobachten Sie die Fehlermeldungen, die Sie erhalten:
# - Lassen Sie ein Anführungszeichen in einem String weg.
# - Lassen Sie beide Anführungszeichen in einem String weg.
# - Schreiben Sie das Wort `print` falsch.
# - Lassen Sie eine Klammer weg, oder beide.

# %%
# Try out the intentional mistakes here. For example:
print("Hello, world!
# (You can add more cells as needed to try each mistake)

# %% [markdown] lang="en" tags=["subslide"]
# **Exercise 2**: What happens if you:
# - Use a minus sign to make a negative number?
# - Put a plus sign before a number?
# - Try to use leading zeros in a number, like `09` or `011`?
# - Have two values with no operator between them?
# 
# Experiment in the cells below:

# %% [markdown] lang="de" tags=["subslide"]
# **Übung 2**: Was passiert, wenn Sie:
# - Ein Minuszeichen verwenden, um eine negative Zahl zu erstellen?
# - Ein Pluszeichen vor einer Zahl setzen?
# - Versuchen, führende Nullen in einer Zahl zu verwenden, wie `09` oder `011`?
# - Zwei Werte ohne Operator dazwischen haben?
# 
# Experimentieren Sie in den folgenden Zellen:

# %%
# Experiment with the mentioned scenarios here:

