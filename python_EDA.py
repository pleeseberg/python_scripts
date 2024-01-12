import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def eda_summary_statistics(df):
    """
    Display summary statistics of the dataset.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    print("Summary Statistics:")
    print(df.describe())

def eda_data_types_missing_values(df):
    """
    Display data types and missing values in the dataset.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

def eda_numerical_distribution(df):
    """
    Display the distribution of numerical features.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns

    for feature in numerical_features:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[feature], kde=True)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()

def eda_visualization(df):
    """
    Visualize key features in the dataset.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    # Add your specific visualization code using Seaborn or Matplotlib
    # Example:
    sns.pairplot(df, hue='target_column')
    plt.title('Pairplot of Key Features')
    plt.show()

# Example Usage:
file_path = 'path/to/your/data/file/data.csv'

# Load data
data_df = pd.read_csv(file_path)

# EDA tasks
eda_summary_statistics(data_df)
eda_data_types_missing_values(data_df)
eda_numerical_distribution(data_df)
eda_visualization(data_df)
