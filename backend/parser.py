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

    required_columns = [
        "Handle",
        "Title",
        "Vendor",
        "Variant SKU",
        "Variant Price",
        "Variant Inventory Qty",
        "Option1 Name",
        "Option1 Value"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    products = {}

    for _,row in df.iterrows():
        handle = row["Handle"]

        if handle not in products:
            products[handle] = {
                "handle": handle,
                "title": row["Title"],
                "vendor": row["Vendor"],
                "variants":[]

            }
        variant = {
            "sku": row["Variant SKU"],
            "price": row["Variant Price"],
            "inventory": row["Variant Inventory Qty"],
            "option_name": row["Option1 Name"],
            "option_value": row["Option1 Value"]
        }
        products[handle]["variants"].append(variant)
    return products

