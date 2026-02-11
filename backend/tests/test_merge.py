import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from merge import merge_product, merge_variant


def test_merge_product_keeps_existing_when_incoming_none():
    existing = {"handle": "shirt-basic", "title": "Old", "vendor": "Acme"}
    incoming = {"handle": "shirt-basic", "title": None, "vendor": "NewCo"}

    merged = merge_product(existing, incoming)

    assert merged["title"] == "Old"
    assert merged["vendor"] == "NewCo"


def test_merge_variant_updates_or_adds():
    existing_variants = [
        {"sku": "TS-S", "price": 19.99, "inventory": 10},
    ]
    incoming_update = {"sku": "TS-S", "price": 21.99, "inventory": 15}
    incoming_new = {"sku": "TS-M", "price": 21.99, "inventory": 20}

    merge_variant(existing_variants, incoming_update)
    merge_variant(existing_variants, incoming_new)

    assert len(existing_variants) == 2
    assert existing_variants[0]["price"] == 21.99
    assert existing_variants[1]["sku"] == "TS-M"
