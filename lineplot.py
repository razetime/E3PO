import pandas as pd
import matplotlib.pyplot as plt
import json

with open('/home/khin/bytedance/E3PO2/e3po/result/group_1/v2_s1/erp/evaluation.json', 'r') as file:
    data = json.load(file)


# We only need the first part of the JSON data, which contains the frame data
frames_data = data[:-1]  # Exclude the last item which is the summary

# Initialize lists to hold our data
frame_indices = []
psnr_values = []

# Extract data
for frame_list in frames_data:
    for frame in frame_list:
        frame_indices.append(frame['frame_idx'])
        psnr_values.append(frame['psnr'])

# Create a DataFrame
df = pd.DataFrame({
    'Frame Index': frame_indices,
    'PSNR': psnr_values
})

plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(df['Frame Index'], df['PSNR'], color='purple', marker='*', linestyle='--', linewidth=1, markersize=5)
plt.title('PSNR across Frames')
plt.xlabel('Frame Number')
plt.ylabel('PSNR (dB)')
plt.grid(True)
plt.tight_layout()
plt.show()
