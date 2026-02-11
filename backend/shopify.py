fake_shopify_db = {}

def get_product(handle):
    """
    Retrieve product by handle 
    Returns product dict or None
    """

    return fake_shopify_db.get(handle)

def create_product(product):

    fake_shopify_db[product["handle"]] = product
    return product

def update_product(product):
    fake_shopify_db[product["handle"]] = product
    return product

def get_all_products():

    return fake_shopify_db