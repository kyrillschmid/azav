# j2 from 'macros.j2' import header
# {{ header("Matplotlib Scatterplots", "Matplotlib Scatterplots") }}

# %% [markdown] lang="en" tags=["slide"]
# # Simple Scatter Plots
# - Scatter plots are a common type of plot similar to line plots.
# - Instead of joining points with line segments as in line plots, scatter plots represent individual points with dots, circles, or other shapes.
# - In this section, we'll start by setting up the notebook for plotting and importing the necessary modules.
# - We'll then dive into creating scatter plots using Matplotlib.

# %%
# Importing necessary libraries
import matplotlib.pyplot as plt

# Setting plot style
plt.style.use("seaborn-whitegrid")

import numpy as np

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with `plt.plot`
# - plt.plot can also be used to create scatter plots
# - This is done by modifying the third argument for the function
# - Here, we can use character codes to define the nature of the plot
# - For instance, 'o' would generate a dot plot.
# - Let's dive into some examples.# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with plt.plot
# - In addition to line plots, the `plt.plot` function can be used to generate scatter plots
# - The third argument in the function call defines the type of marker used for the plotting
# - Just like line style can be controlled using options such as '-', '--', the marker style can be controlled using string codes
# - These marker style codes and their inputs can be seen in the `plt.plot` documentation

# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.plot(x, y, "o", color="black")

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plot Markers
# - There are numerous types of markers that can be used in scatter plots
# - We can present a few examples like 'o', '.', ',', 'x', '+', 'v', etc.
# - Beyond these, you can use a mix of line, color and character codes to design more complex plots
# - The `plt.plot` function offers flexibility for a wide range of visualization options

# %%
rng = np.random.RandomState(0)
for marker in ["o", ".", ",", "x", "+", "v", "^", "<", ">", "s", "d"]:
    plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

# %%

plt.plot(x, y, "-ok")

# %% [markdown] lang="en" tags=["slide"]
# ## Properties of Lines and Markers
# - There are additional keyword arguments to `plt.plot` that help specify various properties of lines and markers
# - For example, color, markersize, linewidth, etc.
# - These properties allow the user to craft detailed, personalized visualizations using matplotlib
# - Please refer the `plt.plot` documentation for a complete list of the options available.

# %%
plt.plot(
    x,
    y,
    "-p",
    color="gray",
    markersize=15,
    linewidth=4,
    markerfacecolor="white",
    markeredgecolor="gray",
    markeredgewidth=2,
)
plt.ylim(-1.2, 1.2)

# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with plt.scatter
# - Beyond `plt.plot`, matplotlib provides another function for creating scatter plots, `plt.scatter`
# - The `plt.scatter` function provides some advantages over `plt.plot` for certain use-cases but also has its limitations
# - In the following section, we will explore scatter plots using `plt.scatter` in more detail
# %% [markdown] lang="en" tags=["slide"]
# ## Scatter Plots with `plt.scatter`
# - `plt.scatter` is a powerful tool for creating scatter plots and is similar in use to `plt.plot`
# - The unique aspect about `plt.scatter` is that it allows customization of each individual point (size, color, edge color)
# - It can be used to represent multidimensional data where various properties of points convey different dimensions
# - For instance, color and size can be set to different variables, enabling visualisation of more than two variables per scatter plot

# %%
plt.scatter(x, y, marker="o")  # basic usage of plt.scatter

# %% [markdown] lang="en" tags=["slide"]
# - To demonstrate its capabilities, let's plot a random scatter plot with points of many colors and sizes
# - We also use the `alpha` parameter to adjust the transparency level to visibly see overlapping points
# - The `color` argument is mapped to a color scale which can be shown using `colorbar()` command
# - The `size` argument specifies the size of points in pixels

# %%
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()  # show color scale

# %% [markdown] lang="en" tags=["slide"]
# - For example, let's visualize Iris data from Scikit-Learn that has petal and sepal sizes of three types of flowers
# - We can plot the sepal length and width on x, y axes, the petal width can be tied to the size of each point, and the type of flower tied to the color of each point
# - Multicolor and multifeature scatter plots like this can be very useful for data exploration and presentation

# %%
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T

plt.scatter(
    features[0],
    features[1],
    alpha=0.2,
    s=100 * features[3],
    c=iris.target,
    cmap="viridis",
)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# %% [markdown] lang="en" tags=["slide"]
# ## `plot` Versus `scatter`: A Note on Efficiency
# - It is important to note the difference in efficiency between `plt.plot` and `plt.scatter`
# - Although `plt.scatter` allows high level of customization, it can be close to an order of magnitude slower than `plt.plot`
# - Therefore, for large datasets, it is recommended to favor `plt.plot` over `plt.scatter` whenever possible# %% [markdown] lang="en" tags=["slide"]
# ## `plot` Versus `scatter`: A Note on Efficiency
# - Both `plt.plot` and `plt.scatter` are used to graph data but their usage depends upon the size of data.
# - For smaller datasets, the difference in performance between `plt.plot` and `plt.scatter` isn't quite significant.
# - However, as datasets become larger (more than a few thousand points), `plt.plot` can be more efficient due to the way it renders data points.

# %% [markdown] lang="en" tags=["slide"]
# ## Details about `scatter` and `plot`
# - The `plt.scatter` function has the capability to render different size and/or color for each point, therefore, it constructs each point individually.
# - On the other hand, in `plt.plot`, the data points are clones of each other, so it determines the appearance of the points only once for the whole set.
# - Due to this fundamental difference, `plt.plot` offers better performance for large datasets and is generally preferred over `plt.scatter` in such scenarios.
