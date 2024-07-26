import pytest
# TODO: add necessary import
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    #Checking if the Number of Columns Match the Number of Columns in the Source File
    """
    # Your code here
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    num_of_columns = 15
    columns_read = data.shape[1]

    assert num_of_columns == columns_read


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    #Checking if the Number of Rows Match the Number of Rows in the Source File
    """
    # Your code here
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    num_of_rows = 32561
    rows_read = data.shape[0]

    assert num_of_rows == rows_read


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    expected_columns = [
        "age",
        "workclass",
        "fnlgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "salary"
    ]

    column_names_read = data.columns.tolist()

    assert expected_columns == column_names_read
