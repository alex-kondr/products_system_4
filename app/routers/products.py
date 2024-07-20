from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files
from app.keyboards.products import build_products_keyboard, build_product_actions_keyboard


product_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@product_router.message(F.text == "Список товарів")
async def show_products(message: Message, state: FSMContext):
    products = open_files.get_products()
    keyboard = build_products_keyboard(products)
    await edit_or_answer(
        message=message,
        text="Список товарів",
        keyboard=keyboard
    )


@product_router.callback_query(F.data.startswith("product_"))
async def product_actions(call_back: CallbackQuery, state: FSMContext):
    prod_index = call_back.data.split("_")[-1]
    product = open_files.get_product(prod_index)
    keyboard = build_product_actions_keyboard(prod_index)
    await edit_or_answer(
        message=call_back.message,
        text=product,
        keyboard=keyboard
    )