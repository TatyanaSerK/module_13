from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ''
bot = Bot(token= api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    # start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
    # Запускается только когда написана команда '/start' в чате с ботом.
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler(text = 'Calories')# реагирует на текстовое сообщение 'Calories'.
async def set_age(message):    # функция выводит вTelegram - бот сообщение'Введите свой возраст:'.
    await message.answer("Введите свой возраст:")
    await UserState.age.set() # После ожидать ввода возраста в атрибут UserState.age при помощи метода set.


@dp.message_handler(state=UserState.age)#реагирует на переданное состояние UserState.age.
async def set_growth(message, state):
# функция должна обновлять данные в состоянии age на message.text
# Далее должна выводить в Telegram - бот сообщение 'Введите свой рост:'.
# После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)# реагирует  на переданное  состояние   UserState.growth.
async def set_weight(message, state):
# Эта функция должна обновлять данные в состоянии growth на message.text
# Далее должна выводить в Telegram - бот сообщение'Введите свой вес:'.
# После ожидать ввода роста в атрибут UserState.weightпри помощи метода set
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)# реагирует на переданное состояние UserState.weight.
async def send_calories(message, state):
# Эта функция должна обновлять данные в состоянии weight наmessage.text
    await state.update_data(weight=message.text)
    date = await state.get_data()# запомните в переменную data все ранее введённые состояния
# упрощённую формулу Миффлина-Сан Жеора для подсчёта нормы калорий(для женщин)
    kalorii = 10*int(date['weight']) + 6.25*int(date['growth']) - 5*int(date['age']) - 161
    await message.answer(f"Ваша норма калорий: {kalorii}")# Результат вычисления по формуле .
    await state.finish()# Финишируйте машину состояний методомfinish().

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
