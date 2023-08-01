import pandas as pd
import pytest

from stock_data_analysis import clean_data

@pytest.fixture
def sample_data():
    data = {
        'Date': ['2023-01-01', '2023-01-02'],
        'Open': ['$100.50', '$99.75'],
        'High': ['$101.20', '$100.50'],
        'Low': ['$99.25', '$99.00'],
        'Close/Last': ['$101.00', '$100.00'],
        'Volume': [100000, 120000]
    }
    return pd.DataFrame(data)

def test_clean_data(sample_data):
    df = clean_data(sample_data)

    # Check if the original DataFrame is not modified
    assert 'Date' in sample_data.columns
    assert 'Open' in sample_data.columns
    assert 'High' in sample_data.columns
    assert 'Low' in sample_data.columns
    assert 'Close/Last' in sample_data.columns
    assert 'Volume' in sample_data.columns

    # Check if the cleaned DataFrame has the correct data types
    assert df['Open'].dtype == float
    assert df['High'].dtype == float
    assert df['Low'].dtype == float
    assert df['Close/Last'].dtype == float

    # Check if the dollar signs are removed and the values are correctly converted to float
    assert df['Open'].equals(pd.Series([100.50, 99.75], name='Open'))
    assert df['High'].equals(pd.Series([101.20, 100.50], name='High'))
    assert df['Low'].equals(pd.Series([99.25, 99.00], name='Low'))
    assert df['Close/Last'].equals(pd.Series([101.00, 100.00], name='Close/Last'))

    # Check if the original DataFrame remains unchanged after the function call
    assert 'Open' in sample_data.columns
    assert 'High' in sample_data.columns
    assert 'Low' in sample_data.columns
    assert 'Close/Last' in sample_data.columns
    assert 'Volume' in sample_data.columns
    assert df['Volume'].equals(sample_data['Volume'])  # Compare with the original DataFrame
