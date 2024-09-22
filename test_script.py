import pytest
from script import generate_summary, visualize_data, read_data
import pandas as pd
from io import StringIO

# Mock data
data_string = """Year,Incidents
2020,5
2021,10
2022,15
"""
mock_data = pd.read_csv(StringIO(data_string))

# Patch the read_data function to return mock_data instead of reading from a file
def test_read_data(monkeypatch):
    def mock_read_data(file_path):
        return mock_data
    monkeypatch.setattr('script.read_data', mock_read_data)
    assert read_data("dummy_path").equals(mock_data)

def test_generate_summary(capfd):  # capfd is a pytest fixture that captures stdout and stderr
    generate_summary(mock_data)
    out, err = capfd.readouterr()
    assert "2020" in out
    assert "2021" in out
    assert "mean" in out

# Visualization testing can be tricky as it generally requires visual inspection
# For automation, you might consider checking if the file is created or not
def test_visualize_data(tmp_path, monkeypatch):
    # Redirect output to temporary path
    monkeypatch.setattr(plt, 'savefig', lambda filename: plt.savefig(tmp_path / 'test_incident_years_histogram.png'))
    visualize_data(mock_data)
    assert (tmp_path / 'test_incident_years_histogram.png').exists()
