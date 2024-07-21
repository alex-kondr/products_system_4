import json

from app.data import list_files, open_files


def remove_product(prod_index: int) -> str:
    products = open_files.get_products()
    product = products.pop(prod_index)

    with open(list_files.PRODUCTS, "w", encoding="utf-8") as file:
        json.dump(products, file)

    msg = f"Товар '{product}' успішно видалено."
    return msg


def sold_product(prod_index: int) -> str:
    products = open_files.get_products()
    product = products.pop(prod_index)

    sold_products = open_files.get_sold_products()
    sold_products.append(product)

    with open(list_files.PRODUCTS, "w", encoding="utf-8") as file:
        json.dump(products, file)

    with open(list_files.SOLD_PRODUCTS, "w", encoding="utf-8") as file:
        json.dump(sold_products, file)

    msg = f"Товар '{product}' успішно продано. Дякую за покупку."
    return msg


def add_product(product: str) -> str:
    products = open_files.get_products()

    if product in products:
        msg = f"Товар '{product}' вже є у списку."
        return msg

    products.append(product)

    with open(list_files.PRODUCTS, "w", encoding="utf-8") as file:
        json.dump(products, file)

    msg = f"Товар '{product}' успішно доданий."
    return msg