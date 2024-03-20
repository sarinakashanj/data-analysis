import pandas as pd

# Specify the path to your CSV file
csv_file_path = "Analysis.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# List of participant IDs
participant_ids = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10',
                   'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', 'P19', 'P20']

# List of tasks
tasks = ['T1', 'T2', 'T3', 'T4', 'T5']

# List of WF conditions
wfs = ['WF1', 'WF2']

# Initialize a list to store the data
data = []

# Calculate mean values for each participant, task, and WF condition
for participant_id in participant_ids:
    for task in tasks:
        for wf in wfs:
            # Filter DataFrame based on the condition
            filtered_df = df[(df['Task'] == task) & (df['WF'] == wf) & (df['P ID'] == participant_id)]
            
            # Calculate mean of the 'Time' column in the filtered DataFrame
            mean_value = filtered_df['Time'].mean()
            
            # Append the results to the data list
            data.append({
                'P ID': participant_id,
                'Task': task,
                'WF': wf,
                'Average Time': mean_value
            })

# Create a DataFrame from the data list
results_df = pd.DataFrame(data)

# Save results to a new CSV file
results_df.to_csv("mean_results_combined.csv", index=False)

print("Results saved to mean_results_combined.csv")
