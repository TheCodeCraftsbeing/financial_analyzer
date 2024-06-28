# modules/data_input.py

import pandas as pd

def load_from_file(file_path):
    """
    Load financial data from a text file.
    """
    data = pd.read_csv(file_path)
    return data
