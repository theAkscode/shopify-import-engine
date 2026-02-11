def merge_product(existing_product, incoming_product):
    for key, value in incoming_product.items():
        if key == "variants":
            continue
        if value is not None:
            existing_product[key] = value
    return existing_product


def merge_variant(existing_variants, incoming_variant):
    incoming_sku = incoming_variant.get("sku")

    if not incoming_sku:
        existing_variants.append(incoming_variant)
        return existing_variants

    for variant in existing_variants:
        if variant.get("sku") == incoming_sku:
            for key, value in incoming_variant.items():
                if value is not None:
                    variant[key] = value
            return existing_variants

    existing_variants.append(incoming_variant)
    return existing_variants
