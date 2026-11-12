from display import print_products_menu
from functions import user_choice
from data import *
from validations import validate_user_input


def product_management():
    while True:
        print_products_menu()
        choice = user_choice("Enter your choice (1-6): ")
        match choice:
            case 1:
                add_product()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                update_product()
            case 5:
                delete_product()
            case 6:
                break
            case _ :
                print("please choose between 1-6")

def add_product():
    name = validate_user_input("Enter product name: ", "str")
    if chack_product_exists(products, "name", name):
        print(f"Product '{name}' already exists.")
        return
    category = validate_user_input("Enter product category: ", "str")
    price = validate_user_input("Enter product price: ", "positive_float")
    stock = validate_user_input("Enter product stock: ", "positive_num")
    new_product = create_product(len(products)+1, name, category, price, stock, True)
    add_product_to_products(products, new_product)
    print(f"Product '{name}' added successfully.")

def view_products():
    print_product(products)

def print_product(products,message="No products available."):
    if not products:
        print(message)
        return
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}, Active: {product['active']}")

def search_product():
    list_of_options = ["id", "name", "category"]
    search_type = validate_user_input("Search by (id/name/category): ", "str").lower()
    if search_type not in list_of_options:
        print(f"Invalid search type. Please choose (id/name/category).")
        return
    search_value = validate_user_input(f"Enter {search_type}: ", "not_empty")
    found_products = []
    for product in products:
        if search_value.lower() in str(product[search_type]).lower():
            found_products.append(product)
    print_product(found_products,f"No products found with {search_type} '{search_value}'.")
    
