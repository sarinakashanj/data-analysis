import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Specify the path to your CSV file
csv_file_path = "Analysis.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# List of tasks
tasks = ['T1', 'T2', 'T3', 'T4', 'T5']

# Initialize dictionaries to store the average time for each WF condition
average_times_wf1 = {}
average_times_wf2 = {}

# Calculate mean values for each task when WF == 'WF1'
for task in tasks:
    filtered_df_wf1 = df[(df['Task'] == task) & (df['WF'] == 'WF1')]
    average_times_wf1[task] = filtered_df_wf1['Time'].mean()
    
# Calculate mean values for each task when WF == 'WF2'
for task in tasks:
    filtered_df_wf2 = df[(df['Task'] == task) & (df['WF'] == 'WF2')]
    average_times_wf2[task] = filtered_df_wf2['Time'].mean()

# Convert average times to lists for plotting
avg_times_wf1 = [average_times_wf1[task] for task in tasks]
avg_times_wf2 = [average_times_wf2[task] for task in tasks]

# Set the positions of the bars
x = np.arange(len(tasks))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, avg_times_wf1, width, label='WF1')
rects2 = ax.bar(x + width/2, avg_times_wf2, width, label='WF2')

# Add some text for labels, title, and custom x-axis tick labels
ax.set_xlabel('Task')
ax.set_ylabel('Average Time')
ax.set_title('Average Time by Task and WF Condition')
ax.set_xticks(x)
ax.set_xticklabels(tasks)
ax.legend()

# Function to auto-label the bars, if desired
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(round(height, 2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Call the function to label the bars
autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
