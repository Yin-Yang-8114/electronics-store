products = []


def create_product(id, name, category, price, stock, active):
    return {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
        "active": active}

def add_product_to_products(products, product):
    products.append(product)

def chack_product_exists(products, serching_type, serching_value):
    for product in products:
        if product[f"{serching_type}"] == serching_value:
            return True
    return False

def get_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

