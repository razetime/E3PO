import matplotlib.pyplot as plt

# GC scores and versions
gc_scores = [5.184791, 6.014892, 5.310066]
versions = ['v1_s1', 'v2_s1', 'v3_s1']

# Creating the bar chart
plt.figure(figsize=(10, 7), facecolor='lightgray')  # Added a light gray background for the figure
bars = plt.bar(versions, gc_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c'], edgecolor='black')

# Adding a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding titles and labels
plt.title('GC Scores for Different Videos', fontsize=15, fontweight='bold')
plt.xlabel('Video ID', fontsize=12)
plt.ylabel('GC Score', fontsize=12)
plt.ylim(4.5, 6.5)  # Adjust the y-axis limits

# Adding text labels above the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Show the plot with enhancements
plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()
