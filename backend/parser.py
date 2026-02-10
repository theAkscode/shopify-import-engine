import pandas as pd

def parse_file(upload_file):
    """
    Reads a CSV or Excel file and groups rows into products with variants.
    Returns a dictionary keyed by product handle.
    """
    filename=upload_file.filename.lower()

    if filename.endswith('.csv'):

        df = pd.read_csv(upload_file.file)
    else: 
        df = pd.read_excel(upload_file.file)
