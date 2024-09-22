import pytest
from lib import read_data, generate_summary, visualize_data
import pandas as pd
from pandas.testing import assert_frame_equal
from unittest.mock import patch
import os
import matplotlib.pyplot as plt


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
    assert len(summary['head']) == 4  # Checks if head returns the default number of rows
    
# Test for visualize_data function
@patch('matplotlib.pyplot.savefig')
def test_visualize_data(mock_savefig, tmp_path):
    # 准备数据
    mock_data = pd.DataFrame({
        'Year': [2020, 2021, 2022, 2023],
        'Incidents': [5, 10, 15, 20]
    })
    # 调用函数
    visualize_data(mock_data, filename=tmp_path / 'test_histogram.png')
    # 检查是否正确调用了 mock_savefig
    mock_savefig.assert_called_once_with(tmp_path / 'test_histogram.png')
    

