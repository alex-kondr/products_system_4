from aiogram.fsm.state import State, StatesGroup


class ProductForm(StatesGroup):
    name = State()