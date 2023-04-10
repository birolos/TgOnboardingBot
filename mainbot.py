import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
import asyncio

# Объект бота
bot = Bot(token="5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

@dp.message_handler(commands="test2")
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)