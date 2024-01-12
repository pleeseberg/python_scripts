import pandas as pd

def clean_data(df):
    """
    Preprocess and clean the data for analysis.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    - cleaned_df (DataFrame): Cleaned Pandas DataFrame.
    """
    # Handle missing values (imputation or removal)
    df = handle_missing_values(df)

    # Remove duplicates
    df = remove_duplicates(df)

    # Outlier detection and removal (customize as needed)
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    df = remove_outliers(df, numerical_features)

    # Convert data types if needed (customize as needed)
    df = convert_data_types(df)

    return df

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    - df (DataFrame): DataFrame with missing values handled.
    """
    # Example: Impute missing values with the mean for numerical columns
    df.fillna(df.mean(), inplace=True)

    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    - df (DataFrame): DataFrame with duplicates removed.
    """
    df.drop_duplicates(inplace=True)
    return df

def remove_outliers(df, numerical_features):
    """
    Remove outliers from numerical features in the DataFrame.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - numerical_features (list): List of numerical feature column names.

    Returns:
    - df (DataFrame): DataFrame with outliers removed.
    """
    # Customize the outlier removal method (e.g., Z-score, IQR) based on your data
    for feature in numerical_features:
        z_scores = (df[feature] - df[feature].mean()) / df[feature].std()
        df = df[(z_scores.abs() < 3)]  # Example: Keep data points within 3 standard deviations

    return df

def convert_data_types(df):
    """
    Convert data types of columns if needed.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    - df (DataFrame): DataFrame with converted data types.
    """
    # Example: Convert a column to datetime format
    # df['date_column'] = pd.to_datetime(df['date_column'])

    return df

# Example Usage:
file_path = 'path/to/your/data/file/data.csv'

# Load data
data_df = pd.read_csv(file_path)

# Clean data
cleaned_data_df = clean_data(data_df)

# Display cleaned data
print("Cleaned Data:")
print(cleaned_data_df.head())
