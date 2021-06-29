# -*- coding: utf-8 -*-
"""
Description : Tutorial on how to add error bars to matplotlib barplot
Ref : https://pythonforundergradengineers.com/python-matplotlib-error-bars.html
"""


# Import Libraries -----------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# Data ------------------------------------------------------------------------
np.random.seed(1)
aluminum = np.random.uniform(1, 10, 10)
copper = np.random.uniform(1, 10, 10)
steel = np.random.uniform(1, 10, 10)

# Calculate Mean --------------------------------------------------------------
aluminum_mu = aluminum.mean()
copper_mu = copper.mean()
steel_mu = steel.mean()

# Calculate the Standard Deviation --------------------------------------------
aluminum_std = np.std(aluminum)
copper_std = np.std(copper)
steel_std = np.std(steel)

# Build Plot ------------------------------------------------------------------
x_labels = ['Aluminim', 'Copper', 'Steel']
x_pos = np.arange(len(x_labels))
cte_s = [aluminum_mu, copper_mu, steel_mu]
error = [aluminum_std, copper_std, steel_std]

# Create Figure & Ax Object
fig, ax = plt.subplots()

# All Features Get Added to Ax
'''x_pos = array with count of number of bars.  Here it = [0,1,2]
'''
rect1 = ax.bar(x_pos, cte_s, yerr=error, align='center', alpha=0.5, ecolor='black',
       capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
       height = rect.get_height()
       ax.text(x = rect.get_x(), y = height*1.25,
               s = '%d' % int(height),
       ha='center', va='bottom')
autolabel(rect1)
# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()








