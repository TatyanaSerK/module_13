from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = ''
bot = Bot(token= api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
#создаем клавиатуру с двумя кнопками(размер подстраиваемый)
button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button1, button2)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    # start(message) - присылает клавиатуру с двумя кнопками
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')# реагирует на нажатие кнопки "рассчитать".
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


@dp.message_handler()
async def all_massages(message):
    # all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
    # Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
