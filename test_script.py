import pytest
from script import generate_summary, visualize_data, read_data
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns


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
    # 正确覆盖 pandas 的 read_excel 函数
    with patch('pandas.read_excel', return_value=mock_data) as mock_func:
        result = read_data("dummy_path")
        assert result.equals(mock_data)
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
    # 导入 plt 后，正确设置 monkeypatch
    def mock_savefig(filename):
        plt.savefig(tmp_path / 'test_incident_years_histogram.png')

    monkeypatch.setattr(plt, 'savefig', mock_savefig)
    visualize_data(some_data_frame)  # 确保 some_data_frame 是您测试数据的一个实例
    assert (tmp_path / 'test_incident_years_histogram.png').exists()
