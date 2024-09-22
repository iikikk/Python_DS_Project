import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(file_path, sheet_name='Sheet1'):
    """
    Reads data from an Excel file and returns a pandas DataFrame.

    Parameters:
    - file_path: str, the path to the Excel file.
    - sheet_name: str, the name of the sheet to read.

    Returns:
    - DataFrame containing the data from the specified Excel sheet.
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def generate_summary(data):
    """
    Generates and returns summary statistics for the given DataFrame.

    Parameters:
    - data: DataFrame, the data for which summary statistics are computed.

    Returns:
    - dict containing various summary statistics.
    """
    summary_stats = {
        "head": data.head(),
        "dtypes": data.dtypes,
        "describe": data.describe(include='all'),
        "year_stats": data['Year'].agg(['mean', 'median', 'std'])
    }
    return summary_stats

def visualize_data(data, filename='incident_years_histogram.png'):
    """
    Generates and saves a histogram of the 'Year' column of the DataFrame.

    Parameters:
    - data: DataFrame, the data used for generating the histogram.
    - filename: str, the filename where the histogram image will be saved.

    Effects:
    - Saves a histogram plot to the specified filename.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Year'], kde=False, color='blue')
    plt.title('Distribution of Incident Years')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
