from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список товарів")
    builder.button(text="Додати новий товар")
    builder.button(text="Показати список проданий товарів")
    builder.button(text="Додати відгук")
    builder.button(text="Показати всі відгуки")
    builder.adjust(1)
    return builder.as_markup()