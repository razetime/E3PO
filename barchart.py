import matplotlib.pyplot as plt
import json
import numpy as np

# constants from e3po.yml
gc_w1 = 0.09                           # parameter w1 for calculating grand challenge score
gc_w2 = 0.000015                       # parameter w2 for calculating grand challenge score
gc_w3 = 0.000334                       # parameter w3 for calculating grand challenge score
gc_alpha = 0.006                       # parameter alpha for calculating grand challenge score
gc_beta = 10                           # parameter beta for calculating grand challenge score

def get_S(b,s,c,mse):
    # S = 1/((alpha*MSE)+(beta*((w1*Cb)+(w2*Cs)+(w3*Cc))) 
    return 1.0/((gc_alpha*mse)+gc_beta*(gc_w1*b+gc_w2*s+gc_w3*c))

videos = ['v1_s1', 'v1_s2', 'v3_s1']
approaches = {"erp": [], "erp_lstm": []}

x = np.arange(len(videos))  # the label locations
width = 0.25

fig, ax = plt.subplots(layout='constrained', facecolor='lightgray')

for video in videos:
    # GC scores and versions
    for approach, vals in approaches.items():
        with open(f'./e3po/result/group_1/{video}/{approach}/evaluation.json', 'r') as file:
            data = json.load(file)[-1]
        vals.append(float(data["GC Score"]))

multiplier = 0
for approach, measurement in approaches.items():
    offset = width*multiplier
    rects = ax.bar(x + offset, measurement, width, label=approach)
    ax.bar_label(rects, padding=3)
    multiplier += 1
    
print(approaches)

# # Adding a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding titles and labels
ax.set_title('GC Scores for Different Videos')
ax.set_xlabel('Video ID')
ax.set_ylabel('GC Score')
ax.set_xticks(x + width, videos)
ax.legend(loc='upper left', ncols=3)
# plt.ylim(4.5, 6.5)  # Adjust the y-axis limits

# # Adding text labels above the bars
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Show the plot with enhancements
plt.tight_layout()  # Adjust subplot parameters to give specified padding

plt.savefig("plots/ppt_lstm_1.png")
