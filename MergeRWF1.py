import pandas as pd

# Specify the path to your CSV file
csv_file_path = "Analysis.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# List of tasks
tasks = ['T1', 'T2', 'T3', 'T4', 'T5']

# List of WF conditions
wfs = ['WF1', 'WF2']

# Initialize a list to store the data
data = []

# Iterate over both WF conditions and tasks to calculate mean values
for wf in wfs:
    for task in tasks:
        # Filter DataFrame based on the current WF condition and task
        filtered_df = df[(df['Task'] == task) & (df['WF'] == wf)]
        
        # Calculate mean of the 'Time' column in the filtered DataFrame
        mean_value = filtered_df['Time'].mean()
        
        # Append the results to the data list
        data.append({
            'Task': task,
            'WF': wf,
            'Average Time': mean_value
        })

# Create a DataFrame from the data list
results_df = pd.DataFrame(data)

# Save results to a new CSV file
results_df.to_csv("mean_results_combined2.csv", index=False)

print("Results saved to mean_results_combined2.csv")
