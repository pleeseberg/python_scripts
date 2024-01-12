import pandas as pd

# Load your dataset
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the actual file path or URL of your dataset

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())

# Perform basic statistical analysis
print("\nStatistical Summary:")
print(data.describe())

# Filter data based on a condition
filtered_data = data[data['Column_Name'] > 50]  # Replace 'Column_Name' with the actual column name and 50 with your condition
print("\nFiltered Data:")
print(filtered_data.head())

# Group data and calculate aggregate statistics
grouped_data = data.groupby('Category_Column')['Numeric_Column'].mean()  # Replace 'Category_Column' and 'Numeric_Column' with actual column names
print("\nGrouped Data:")
print(grouped_data)

# Save the results to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)  # Replace 'filtered_data.csv' with the desired output file name
print("\nFiltered data saved to 'filtered_data.csv'")
