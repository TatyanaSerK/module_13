from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7361297831:AAGgvYRVs--JZkSRaoZIujfZrZUCUs10Hbc'
bot = Bot(token= api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    # start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
    # Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
    print("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_massages(message):
    # all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
    # Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
    print("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)