from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()

    for index, product in enumerate(products):
        builder.button(text=product, callback_data=f"product_{index}")

    builder.adjust(4)
    return builder.as_markup()


def build_product_actions_keyboard(index: str|int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Продати товар", callback_data=f"sold_product_{index}")
    builder.button(text="Видалити товар", callback_data=f"remove_product_{index}")
    return builder.as_markup()
