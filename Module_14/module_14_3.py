from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio


api = input('Вставьте код:')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup(resize_keyboard=True)
kb_products = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
button_product_1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_product_2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_product_3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_product_4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb.add(button)
kb.add(button_2)
kb_products.add(button_product_1)
kb_products.add(button_product_2)
kb_products.add(button_product_3)
kb_products.add(button_product_4)
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
    for i in range(1, 5):
        with open('image.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: Product{i} | Описание: {i} | Цена: {i*100})')
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
