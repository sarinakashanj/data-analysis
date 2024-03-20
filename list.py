import pandas as pd

# Specify the path to your CSV file
csv_file_path = "Analysis.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# List of tasks
tasks = ['T1', 'T2', 'T3', 'T4', 'T5']

# List of WF conditions
wfs = ['WF1', 'WF2']

# Initialize a list to store the data as dictionaries
output_data = []

# Iterate over both WF conditions and tasks to calculate mean values
for wf in wfs:
    for task in tasks:
        # Filter DataFrame based on the current WF condition and task
        filtered_df = df[(df['Task'] == task) & (df['WF'] == wf)]
        
        # Calculate mean of the 'Time' column in the filtered DataFrame
        mean_value = filtered_df['Time'].mean()
        
        # Append the results as a dictionary to the output_data list
        output_data.append({
            'Task': task,
            'WF': wf,
            'Average Time': mean_value
        })

# Iterate over the list of dictionaries and print out the results
for item in output_data:
    print(f"Task: {item['Task']}, WF: {item['WF']}, Average Time: {item['Average Time']}")

# Now, output_data contains all your results in a format that's easy to work with or modify for future needs
