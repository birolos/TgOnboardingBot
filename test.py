import logging

from aiogram import Bot, Dispatcher, executor, types


#configure logging
API_TOKEN = "5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM"
#configure bot and dispathcer
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

#interaction with bots starts with one command. Register your first command handler:

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	"""
	This handler will be called when user sends `/start` or `/help` command
	"""
	await message.reply("Hi\nI'm EchoBot\nPowered by aiogram.")
#run long polling
if __name__ == '__main__':
	executor.start_polling(dp, skipupdates=True)