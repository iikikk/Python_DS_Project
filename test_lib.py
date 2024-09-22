import pytest
from lib import read_data, generate_summary, visualize_data
import pandas as pd
from pandas.testing import assert_frame_equal
from unittest.mock import patch
import os

# Sample data for testing
sample_data = pd.DataFrame({
    'Year': [2020, 2021, 2022, 2023],
    'Incidents': [5, 10, 15, 20]
})

@pytest.fixture
def mock_data():
    return sample_data.copy()

# Test for read_data function
@patch('pandas.read_excel')
def test_read_data(mock_read_excel, mock_data):
    """
    Test whether read_data correctly reads an Excel file.
    """
    mock_read_excel.return_value = mock_data
    result = read_data("dummy_path.xlsx")
    assert_frame_equal(result, mock_data)
    mock_read_excel.assert_called_once_with("dummy_path.xlsx", sheet_name='Sheet1')

# Test for generate_summary function
def test_generate_summary(mock_data):
    """
    Test whether generate_summary correctly generates summary statistics.
    """
    summary = generate_summary(mock_data)
    assert 'head' in summary and 'dtypes' in summary and 'describe' in summary and 'year_stats' in summary
    assert len(summary['head']) == 5  # Checks if head returns the default number of rows
    assert 'Year' in summary['dtypes']  # Check if the right column is analyzed

# Test for visualize_data function
@patch('matplotlib.pyplot.savefig')
def test_visualize_data(mock_savefig, mock_data):
    """
    Test whether visualize_data saves a plot to a file.
    """
    visualize_data(mock_data, 'test_histogram.png')
    mock_savefig.assert_called_once_with('test_histogram.png')
    assert os.path.exists('test_histogram.png')  # Check if the file was created

