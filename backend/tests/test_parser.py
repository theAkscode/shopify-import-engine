import io
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import parse_file


class FakeUploadFile:
    def __init__(self, filename, text):
        self.filename = filename
        self.file = io.StringIO(text)


def test_parse_file_groups_variants():
    csv_text = (
        "Handle,Title,Vendor,Variant SKU,Variant Price,Variant Inventory Qty,"
        "Option1 Name,Option1 Value\n"
        "shirt-basic,Basic Tee,Acme,TS-S,19.99,50,Size,S\n"
        "shirt-basic,Basic Tee,Acme,TS-M,19.99,60,Size,M\n"
    )
    upload = FakeUploadFile("sample.csv", csv_text)

    products = parse_file(upload)

    assert "shirt-basic" in products
    assert products["shirt-basic"]["title"] == "Basic Tee"
    assert len(products["shirt-basic"]["variants"]) == 2


def test_parse_file_missing_column_raises():
    csv_text = (
        "Handle,Title,Variant SKU,Variant Price,Variant Inventory Qty,"
        "Option1 Name,Option1 Value\n"
        "shirt-basic,Basic Tee,TS-S,19.99,50,Size,S\n"
    )
    upload = FakeUploadFile("sample.csv", csv_text)

    try:
        parse_file(upload)
        assert False, "Expected ValueError for missing column"
    except ValueError as exc:
        assert "Missing required column" in str(exc)
