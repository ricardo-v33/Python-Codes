import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['1% NASA ARC Plasma', '5% JHU Plasma', 'Yu et al. (2018)', 'Yu et al. (2017) - N/A']
values = [2.558, 0.894, 0.53, 0]
errors = [0.1054, 0.076, 0.03, 0]  # Error values for each bar

# Create a figure with a high DPI and black background
plt.figure(dpi=2000, facecolor='black')

# Creating the bar chart
x_pos = np.arange(len(categories))

# Set the color of the bars to blue
plt.bar(x_pos, values, yerr=errors, capsize=5, color='dodgerblue', edgecolor='black', ecolor='white')

# Get the current axes and set the background color to black
ax = plt.gca()
ax.set_facecolor('black')

# Set the color of the axes spines to white
ax.spines['top'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white') 

plt.xticks(x_pos, categories, rotation=15)

# Set the axis labels and tick colors to white
ax.tick_params(axis='both', colors='white')
ax.set_xlabel('Samples', color='white')
ax.set_ylabel("Hardness (GPa)", color='white')
ax.set_title("Tholin Hardness and Literature Values", color='white')

# Add grid lines for better readability
plt.grid(axis='y', linestyle='dashed', alpha=0.7, color='white')

# Save the plot as a high-resolution PNG file
plt.savefig('bar_chart_high_quality.png', dpi=2000, bbox_inches='tight')

# Display the plot
plt.show()