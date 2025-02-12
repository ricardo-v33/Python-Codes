# MODULUS & LITERATURE VALUES
# THESE ARE GOING TO BE THE 11/24 5% JHU/PLASMA ON QUARTZ & 9/28 1% NASA ARC/PLASMA SAMPLES

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ["5% NASA ARC on Quartz", "5% JHU on Quartz", 
              "Yu et al. (2018) on Mica", "Yu et al. (2017) on Mica"]
modulus_values = [19.799, 13.179, 10.4, 3]
modulus_errors = [3.127, 1.201, 0.5, 0.5]

# Create a figure with a high DPI and white background
plt.figure(dpi=2000, facecolor="white")

# Creating the bar chart
x_pos = np.arange(len(categories))

# Set the color of the bars to blue
plt.bar(x_pos, modulus_values, yerr=modulus_errors, capsize=5, 
        color="dodgerblue", edgecolor="dodgerblue", ecolor="black", zorder=2, 
        label="Young's Modulus")

# Get the current axes and set the background color to white
ax = plt.gca()
ax.set_facecolor("white")

# Set the color of the axes spines to black
ax.spines["top"].set_color("black")
ax.spines["bottom"].set_color("black")
ax.spines["left"].set_color("black")
ax.spines["right"].set_color("black") 

plt.xticks(x_pos, categories, rotation=15)

# Set the axis labels and tick colors to black
ax.tick_params(axis="both", colors="black")
ax.set_xlabel("Samples", color="black")
ax.set_ylabel("Young's Modulus (GPa)", color="black")
ax.set_title("Young's Modulus for Plasma Tholins", color="black")

# Add grid lines for better readability
plt.grid(axis="y", linestyle="dashed", alpha=0.7, color="black")

# Display the plot
plt.show()
