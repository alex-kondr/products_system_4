import os
import json

from app.data import list_files


if not os.path.exists(list_files.PRODUCTS):
    with open(list_files.PRODUCTS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.SOLD_PRODUCTS):
    with open(list_files.SOLD_PRODUCTS, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.REVIEWS):
    with open(list_files.REVIEWS, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_products(path: str = list_files.PRODUCTS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        products = json.load(file)

    return products


def get_product(prod_index: int) -> str:
    products = get_products()
    return products[prod_index]


def get_sold_products(path: str = list_files.SOLD_PRODUCTS) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        sold_products = json.load(file)

    return sold_products


def get_reviews(path: str = list_files.REVIEWS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
