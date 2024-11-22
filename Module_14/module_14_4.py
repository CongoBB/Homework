from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

# from admin import *
# from db import *
from aiogram.dispatcher import FSMContext
import asyncio

api = input('Вставьте код:')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup(resize_keyboard=True)
kb_products = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
buttons_list = []
for i in range(get_total_products_amount()):
    buttons_list.append(f'button_product_{i+1}')
    buttons_list[i] = InlineKeyboardButton(text=f'Product{i+1}', callback_data='product_buying')
    kb_products.add(buttons_list[i])

kb.add(button)
kb.add(button_2)
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать')],
        [
            KeyboardButton(text='Информация')],
        [
            KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)
# admin_panel = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Пользователи', callback_data='users')],
#         [InlineKeyboardButton(text='Статистика', callback_Data='stat')],
#         [
#             InlineKeyboardButton(text='Блокировка', callback_data='block'),
#             InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
#         ]
#     ]
# )


class UserState(StatesGroup):
    age = State()
    height = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.username}! Я бот, помогающий твоему здоровью.',
                         reply_markup=start_menu)


@dp.message_handler(text=['Купить'])
async def get_product_list(message):
    products = get_all_products()
    for product in products:
        with open(f'{product["title"]}.jpg', 'rb') as img:
            await message.answer_photo(
                img, f'Название: {product["title"]} | Описание: {product["description"]} | Цена: {product["price"]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_msg(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text=['Рассчитать'])
async def start(message):
    await message.answer('Выберите опцию:', reply_markup=kb)


@dp.callback_query_handler(text='calories')
async def infor(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.callback_query_handler(text='formulas')
async def infor(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(text='Информация')
async def set_age(message):
    await message.answer('Рассчитываем дневную норму калорий.')


@dp.message_handler(state=UserState.age)
async def set_height(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.height.set()


@dp.message_handler(state=UserState.height)
async def set_weight(message, state):
    await state.update_data(height=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша дневная норма калорий:"
                         f"{10*int(data['weight']) + 6.25*int(data['height']) - 5*int(data['age']) + 5}")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
