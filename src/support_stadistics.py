import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

def numerical_variables_analysis(df):

    """
    Performs the analysis of numerical variables in the dataset.
    
    This function includes:
    - Descriptive statistics (mean, median, mode, etc.)
    - Outlier identification using the IQR method
    - Correlation analysis through a heatmap visualization

    Parameters:
    -----------
    df : pandas DataFrame
        Input dataset containing numerical variables

    Returns:
    --------
    None
        Prints results and displays a correlation heatmap
    """
    
    # Select only numerical columns from the dataset
    df_num = df.select_dtypes(include=[np.number]).copy()
    
    print("NUMERICAL VARIABLES ANALYSIS\n")
    
    # 1 Descriptive Statistics and Outlier Identification
    for col in df_num.columns:
        
        # Compute mode (handling possible multiple modes or empty results)
        mode = df_num[col].mode()
        mode_value = mode.iloc[0] if not mode.empty else np.nan
        
        # Compute quartiles and IQR for outlier detection
        q1 = df_num[col].quantile(0.25)
        q3 = df_num[col].quantile(0.75)
        iqr = q3 - q1
        
        # Define lower and upper bounds for outliers
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        # Count outliers using the IQR rule
        outliers_count = df_num[(df_num[col] < lower_bound) | (df_num[col] > upper_bound)][col].count()
        
        print(f"Column: {col}")
        print(f"Count: {df_num[col].count()}")
        print(f"Mean: {round(df_num[col].mean(), 2)}")
        print(f"Median: {round(df_num[col].median(), 2)}")
        print(f"Mode: {round(mode_value, 2) if pd.notnull(mode_value) else np.nan}")
        print(f"Standard deviation: {round(df_num[col].std(), 2)}")
        print(f"Minimum: {round(df_num[col].min(), 2)}")
        print(f"Maximum: {round(df_num[col].max(), 2)}")
        print(f"Outliers: {outliers_count}")
        print("-" * 30)
    
    # 2 Correlation Analysis
    print("\nCORRELATION ANALYSIS (HEATMAP)\n")
    
    corr_matrix = df_num.corr()
    
    plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="viridis",
        vmin=-1,
        vmax=1,
        mask=mask,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8})
    
    plt.title("Correlation Matrix", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


def categorical_variables_analysis(df):

    """
    Performs frequency distribution analysis of categorical variables.
    
    This function:
    - Calculates absolute frequency (count)
    - Calculates relative frequency (percentage)
    - Displays results in a tabular format for each categorical variable

    Parameters:
    -----------
    df : pandas DataFrame
        Input dataset containing categorical variables

    Returns:
    --------
    None
        Prints and displays frequency tables for each categorical variable
    """
    
    # Select only categorical columns
    df_cat = df.select_dtypes(include=["object", "category"]).copy()
    
    print("CATEGORICAL VARIABLES ANALYSIS\n")
    
    for col in df_cat.columns:
        
        print(f"Column: {col}")
        
        # Calculate absolute frequencies
        freq = df_cat[col].value_counts(dropna=False)
        
        # Calculate relative frequencies
        perc = (freq / len(df_cat) * 100).round(2)
        
        table = pd.DataFrame({
            "Count": freq,
            "Percentage (%)": perc})
        
        display(table)
        print("-" * 40)