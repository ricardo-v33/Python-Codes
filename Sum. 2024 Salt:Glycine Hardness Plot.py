import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['100%, Hot Plate', '75%, Hot Plate', '50%, Oven', '25%, Oven']
values = [1.046, 1.1673, 0.3719, 2.7798]
errors = [0.1394, 0.1852, 0.0762, 0.9742]  # Error values for each bar

# Create a figure with a high DPI
plt.figure(dpi=2000)  # Increase DPI for higher resolution

# Creating the bar chart
x_pos = np.arange(len(categories))  # Position of bars on x-axis

plt.bar(x_pos, values, yerr=errors, capsize=5, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Concentration')
plt.ylabel("Hardness (GPa)")
plt.title("Salt/Glycine Solution Hardnesses")
plt.xticks(x_pos, categories, rotation=15)

# Adding grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot as a high-resolution PNG file
plt.savefig('bar_chart_high_quality.png', dpi=2000, bbox_inches='tight')  # Save with high DPI and tight bounding box

# Display the plot
plt.show()
