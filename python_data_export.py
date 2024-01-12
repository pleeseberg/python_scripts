import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Function to save cleaned data to a new file
def save_cleaned_data(df, output_path):
    """
    Save cleaned data to a new file.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - output_path (str): Path to save the cleaned data.

    Returns:
    None
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

# Function to export visualizations as images
def export_visualizations(df, output_folder):
    """
    Export visualizations as images.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - output_folder (str): Folder path to save visualizations.

    Returns:
    None
    """
    # Example visualization
    plt.figure(figsize=(10, 6))
    sns.histplot(df['numerical_feature'], kde=True)
    plt.title('Histogram of Numerical Feature')
    plt.xlabel('Numerical Feature')
    plt.ylabel('Frequency')
    plt.savefig(f'{output_folder}/histogram.png')
    plt.close()
    
    print(f"Visualizations saved to: {output_folder}")

# Function to save machine learning model
def save_machine_learning_model(X, y, output_path):
    """
    Save a machine learning model for future use.

    Parameters:
    - X (DataFrame): Features.
    - y (Series): Target variable.
    - output_path (str): Path to save the machine learning model.

    Returns:
    None
    """
    # Example machine learning model (Random Forest)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

    # Save the model
    joblib.dump(model, output_path)
    print(f"Machine learning model saved to: {output_path}")

# Example Usage:
# ... (loading data and previous processing steps)

# Save cleaned data
cleaned_data_output_path = 'path/to/your/cleaned/data/cleaned_data.csv'
save_cleaned_data(cleaned_data_df, cleaned_data_output_path)

# Export visualizations
visualization_output_folder = 'path/to/your/visualization/folder'
export_visualizations(data_df, visualization_output_folder)

# Save machine learning model
X_train, y_train = data_df.drop('target_column', axis=1), data_df['target_column']
machine_learning_model_output_path = 'path/to/your/machine/learning/model/model.joblib'
save_machine_learning_model(X_train, y_train, machine_learning_model_output_path)
