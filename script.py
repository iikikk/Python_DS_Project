import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(file_path):
    """Reads data from an Excel file and returns a pandas DataFrame."""
    return pd.read_excel(file_path, sheet_name='Sheet1')

def generate_summary(data):
    """Generates and prints summary statistics for the given DataFrame."""
    print("First few rows of the dataset:")
    print(data.head())

    print("\nData types of each column:")
    print(data.dtypes)

    statistics = data.describe(include='all')
    print(statistics)

    year_stats = data['Year'].agg(['mean', 'median', 'std'])
    print(f" Summary Statistics for Year:\n{year_stats}")

def visualize_data(data, filename):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Year'], kde=False, color='blue')
    plt.title('Distribution of Incident Years')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(filename)  # 使用传入的 filename 参数
    plt.close()

if __name__ == "__main__":
    file_path = 'TFL Bus Safety.xlsx'
    data = read_data(file_path)
    generate_summary(data)
    visualize_data(data)
