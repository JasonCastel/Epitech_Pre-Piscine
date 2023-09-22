import tkinter
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [6, 5]
plt.rcParams["figure.autolayout"] = True

x =[0,1,2,3]
y = [12,32,42,52]


plt.xlim(0,3)
plt.ylim(10,50)
plt.grid()
plt.scatter(x, y)
plt.show()

