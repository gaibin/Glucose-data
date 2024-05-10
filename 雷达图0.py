import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams['font.sans-serif'] = ['SimHei']  # This line sets the font to SimHei for Chinese characters

# Data
categories = ["Average", "Very Low Blood(%)", "Low Blood(%)", "High Blood(%)", "Very High(%)", "GRI", "TIR"]
data_aerobic = [9.13, 1.27, 2.85, 26.01, 10.23, 47.84, 59.13]
data_resistance = [8.71, 0.00, 0.64, 22.48, 5.77, 28.75, 70.59]
data_mixed = [8.70, 0.00, 0.54, 19.11, 7.70, 28.89, 71.95]

# Set the angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]  # Close the radar chart

# Create a subplot and set it to polar coordinates
fig, ax = plt.subplots(subplot_kw={'polar': True}, figsize=(8, 8))

# Set label font size
plt.rc('font', size=10)

# Define colors
colors = ['#ffb833', '#fc7930', '#4758FB']
cmyk_map = LinearSegmentedColormap.from_list('cmyk', ['cyan', 'magenta', 'yellow', 'black'])
# Draw the radar chart
for i, (label, data) in enumerate(zip(['Aerobic', 'Resistance', 'Mixed'], [data_aerobic, data_resistance, data_mixed])):
    data += data[:1]  # Close the data
    ax.fill(angles, data, colors[i], alpha=0.4, label=label, linewidth=3)
    
    # Annotate key point numbers, slightly adjusted to avoid overlap
    for j in range(len(categories)):
        if categories[j] in ["GRI", "TIR"]:
            ax.annotate(f'{data[j]:.2f}', (angles[j], data[j]), fontsize=15, ha="center", va="center", color=colors[i])
        elif (i == 0 and categories[j] in ["Low Blood(%)", "Very Low Blood(%)"]) or (i != 0 and categories[j] == "Average"):
            # Use a guide line to annotate the specified indicators, the guide line is a little farther, and the number is slightly offset
            angle_rad = angles[j]
            if angle_rad > np.pi:
                angle_rad -= 1 * np.pi
            offset = (0, 0)
            if angle_rad <= np.pi/2:
                offset = (5, 0)
            elif angle_rad <= np.pi:
                offset = (-5, 58)
            elif angle_rad <= 3*np.pi/2:
                offset = (-10, 11)
            else:
                offset = (11, -5)
            ax.annotate(
                f'{data[j]:.2f}',
                xy=(angle_rad, data[j]),
                xytext=(np.sign(angle_rad) * -34 + offset[1], 1.0 + offset[1]),
                textcoords='offset points',
                fontsize=10,
                ha="center",
                va="center",
                arrowprops=dict(arrowstyle="->", color=colors[i], connectionstyle="arc3,rad=0.2"),
            )

# Set coordinate ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=14)
ax.set_yticks([0, 10, 20, 30])  # Set coordinate ticks from 0 to 30
ax.set_yticklabels(["0", "10", "20", "30"], fontsize=13)
#ax.set_title('Radar Chart of 24-Hour Dynamic Blood Glucose Indicators by Training Method', fontsize=12)

# Add legend, set legend position to lower left
plt.legend(loc='lower left')
plt.savefig('radar.pdf', format='pdf')

# Show the radar chart
plt.show()