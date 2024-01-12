import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_numerical_features(df):
    """
    Create visualizations for numerical features.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns

    for feature in numerical_features:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature, y='target_column', data=df)  # Customize 'target_column' as needed
        plt.title(f'Scatter Plot of {feature} vs. target_column')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True)
        plt.title(f'Histogram of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.boxplot(x='target_column', y=feature, data=df)  # Customize 'target_column' as needed
        plt.title(f'Box Plot of {feature} by target_column')
        plt.show()

def visualize_categorical_features(df):
    """
    Create bar charts for categorical features.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    categorical_features = df.select_dtypes(include=['object']).columns

    for feature in categorical_features:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df)
        plt.title(f'Bar Chart of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.show()

def visualize_correlation_matrix(df):
    """
    Create a correlation matrix visualization.

    Parameters:
    - df (DataFrame): Pandas DataFrame.

    Returns:
    None
    """
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

def visualize_time_series(df, time_column):
    """
    Create time series plot if applicable.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - time_column (str): Name of the time column.

    Returns:
    None
    """
    if time_column in df.columns:
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=time_column, y='numerical_feature', data=df)  # Customize 'numerical_feature' as needed
        plt.title(f'Time Series Plot of {time_column} vs. numerical_feature')
        plt.xlabel(time_column)
        plt.ylabel('Numerical Feature')
        plt.show()
    else:
        print(f"{time_column} not found in the dataset. Time series plot not applicable.")

def visualize_pairwise_plots(df, numerical_features):
    """
    Create pairwise scatter plots for numerical features.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - numerical_features (list): List of numerical feature column names.

    Returns:
    None
    """
    sns.pairplot(df[numerical_features])
    plt.suptitle('Pairwise Scatter Plots of Numerical Features', y=1.02)
    plt.show()

def visualize_facet_grids(df, hue_column):
    """
    Create facet grids for visualizing relationships across multiple categorical variables.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - hue_column (str): Categorical variable for color-coding.

    Returns:
    None
    """
    g = sns.FacetGrid(df, col='categorical_column', hue=hue_column, col_wrap=3)
    g.map(sns.scatterplot, 'numerical_feature1', 'numerical_feature2')
    g.add_legend()
    plt.suptitle('Facet Grids of Scatter Plots', y=1.02)
    plt.show()

# Example Usage:
file_path = 'path/to/your/data/file/data.csv'

# Load data
data_df = pd.read_csv(file_path)

# Visualization tasks
visualize_numerical_features(data_df)
visualize_categorical_features(data_df)
visualize_correlation_matrix(data_df)
visualize_time_series(data_df, 'date_column')  # Customize 'date_column' as needed
visualize_pairwise_plots(data_df, ['numerical_feature1', 'numerical_feature2', 'numerical_feature3'])
visualize_facet_grids(data_df, 'target_column')  # Customize 'target_column' as needed
