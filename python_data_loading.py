import pandas as pd

def load_data(file_path=None, file_type=None, sql_query=None):
    """
    Load data from different sources into a Pandas DataFrame.

    Parameters:
    - file_path (str): Path to the data file.
    - file_type (str): Type of the data file (e.g., 'csv', 'excel', 'sql').
    - sql_query (str): Custom SQL query for loading data from SQL databases.

    Returns:
    - df (DataFrame): Pandas DataFrame containing the loaded data.
    """

    if file_type is None:
        raise ValueError("Please provide a file type ('csv', 'excel', 'sql').")

    try:
        if file_type == 'csv':
            df = pd.read_csv(file_path)

        elif file_type == 'excel':
            df = pd.read_excel(file_path)

        elif file_type == 'sql':
            if sql_query is None:
                raise ValueError("Please provide a SQL query for loading data from SQL databases.")
            # Update the connection string as per your SQL database configuration
            # Example: 'sqlite:///example.db'
            connection_string = f'sqlite:///{file_path}'
            df = pd.read_sql_query(sql_query, connection_string)

        else:
            raise ValueError("Invalid file type. Supported types: 'csv', 'excel', 'sql'.")

        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def display_data_preview(df, rows=5):
    """
    Display a preview of the loaded data.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - rows (int): Number of rows to display in the preview.

    Returns:
    None
    """
    print(f"\nData Preview (First {rows} rows):")
    print(df.head(rows))

def display_missing_values(df):
    """
    Display information about missing values in the dataset.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    print("\nMissing Values:")
    print(df.isnull().sum())

# Example Usage:
try:
    file_path = input("Enter the path to your data file: ")
    file_type = input("Enter the type of your data file ('csv', 'excel', 'sql'): ")
    sql_query = input("Enter a custom SQL query (if loading from SQL, otherwise press Enter): ")

    # Load data
    data_df = load_data(file_path, file_type, sql_query)

    if data_df is not None:
        # Display basic information
        display_basic_info(data_df)

        # Display data preview
        display_data_preview(data_df)

        # Display missing values information
        display_missing_values(data_df)

except KeyboardInterrupt:
    print("\nScript terminated by the user.")
except Exception as e:
    print(f"An error occurred: {e}")
