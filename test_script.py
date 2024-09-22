import pytest
from script import generate_summary, visualize_data, read_data
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
from unittest.mock import patch, MagicMock

# Mock data
data_string = """Year,Incidents
2020,5
2021,10
2022,15
"""
mock_data = pd.read_csv(StringIO(data_string))

# Patch the read_data function to return mock_data instead of reading from a file
def test_read_data(monkeypatch):
    mock_data = pd.DataFrame({'data': [1, 2, 3]})
    # 使用 patch 正确导入
    with patch('pandas.read_excel', return_value=mock_data) as mock_func:
        result = read_data("dummy_path")
        assert result.equals(mock_data)  # 确保返回的数据是预期的 mock 数据
        mock_func.assert_called_once_with("dummy_path", sheet_name='Sheet1')

def test_generate_summary(capfd):  # capfd is a pytest fixture that captures stdout and stderr
    generate_summary(mock_data)
    out, err = capfd.readouterr()
    assert "2020" in out
    assert "2021" in out
    assert "mean" in out

# Visualization testing can be tricky as it generally requires visual inspection
# For automation, you might consider checking if the file is created or not
def test_visualize_data(tmp_path, monkeypatch):
    # 为测试准备数据
    test_data = pd.DataFrame({'Year': [2020, 2021, 2022], 'Incidents': [5, 10, 15]})
    # 使用 monkeypatch 覆盖 plt.savefig 方法
    monkeypatch.setattr(plt, 'savefig', MagicMock())
    visualize_data(test_data, filename=tmp_path / 'test_incident_years_histogram.png')
    plt.savefig.assert_called_once()  # 检查是否调用了 savefig
    assert (tmp_path / 'test_incident_years_histogram.png').exists()  # 检查文件是否创建
