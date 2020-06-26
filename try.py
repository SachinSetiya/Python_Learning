# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as nm
import matplotlib.pyplot as plt


# %%
x= nm.linspace(0,15,1000)


# %%
y1= nm.sin(x)


# %%
y2= nm.cos(x)


# %%
plt.plot(x,y1,".")


# %%
plt.plot(x,y2,".")


# %%

plt.show()
