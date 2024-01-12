import pandas as pd
from scipy.stats import ttest_ind, f_oneway, pearsonr, chi2_contingency

def conduct_t_test(df, group_column, numerical_column):
    """
    Conduct independent t-test for group comparisons.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - group_column (str): Column containing group labels.
    - numerical_column (str): Numerical column for comparison.

    Returns:
    None
    """
    groups = df[group_column].unique()

    for i in range(len(groups)-1):
        group1 = groups[i]
        group2 = groups[i+1]

        data_group1 = df[df[group_column] == group1][numerical_column]
        data_group2 = df[df[group_column] == group2][numerical_column]

        t_stat, p_value = ttest_ind(data_group1, data_group2)
        
        print(f"Independent t-test between {group1} and {group2}:")
        print(f"T-statistic: {t_stat}")
        print(f"P-value: {p_value}")
        print("")

def conduct_anova(df, group_column, numerical_column):
    """
    Conduct one-way ANOVA for group comparisons.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - group_column (str): Column containing group labels.
    - numerical_column (str): Numerical column for comparison.

    Returns:
    None
    """
    groups = df[group_column].unique()

    data_groups = [df[df[group_column] == group][numerical_column] for group in groups]

    f_stat, p_value = f_oneway(*data_groups)

    print(f"One-way ANOVA for {numerical_column} across groups:")
    print(f"F-statistic: {f_stat}")
    print(f"P-value: {p_value}")
    print("")

def conduct_correlation_analysis(df, variable1, variable2):
    """
    Conduct correlation analysis between two numerical variables.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - variable1 (str): First numerical variable.
    - variable2 (str): Second numerical variable.

    Returns:
    None
    """
    correlation_coefficient, p_value = pearsonr(df[variable1], df[variable2])

    print(f"Correlation analysis between {variable1} and {variable2}:")
    print(f"Correlation coefficient: {correlation_coefficient}")
    print(f"P-value: {p_value}")
    print("")

def conduct_chi_square_test(df, categorical_column1, categorical_column2):
    """
    Conduct chi-square test for independence for two categorical variables.

    Parameters:
    - df (DataFrame): Pandas DataFrame.
    - categorical_column1 (str): First categorical variable.
    - categorical_column2 (str): Second categorical variable.

    Returns:
    None
    """
    contingency_table = pd.crosstab(df[categorical_column1], df[categorical_column2])

    chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

    print(f"Chi-square test for independence between {categorical_column1} and {categorical_column2}:")
    print(f"Chi-square statistic: {chi2_stat}")
    print(f"P-value: {p_value}")
    print("")

# Example Usage:
file_path = 'path/to/your/data/file/data.csv'

# Load data
data_df = pd.read_csv(file_path)

# Conduct statistical analyses
conduct_t_test(data_df, 'group_column', 'numerical_column')
conduct_anova(data_df, 'group_column', 'numerical_column')
conduct_correlation_analysis(data_df, 'variable1', 'variable2')
conduct_chi_square_test(data_df, 'categorical_column1', 'categorical_column2')
