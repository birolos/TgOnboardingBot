import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile, CallbackQuery, InputMedia
from aiogram.utils.exceptions import BotBlocked
from random import randint
import aiogram.utils.markdown as fmt
import sqlite3
from sqlite3 import Error

bot = Bot(token="5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM")  # Объект бота
dp = Dispatcher(bot)  # Диспетчер для бота
logging.basicConfig(level=logging.INFO)  # Включаем логирование, чтобы не пропустить важные сообщения
floor = 0

@dp.message_handler(commands="start")
async def start_comms(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Информация о нас", callback_data="mainInfo"),
        types.InlineKeyboardButton(text="Продукты компании", callback_data="goods"),
        types.InlineKeyboardButton(text="Сотрудники и Контакты", callback_data="Contacts"),
        types.InlineKeyboardButton(text="Обучение должности", callback_data="job_feats")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Добро пожаловать в Nerv!; ПОЗЖЕ ЗАМЕНИТЬ НА ИНФ ИЗ БД ", reply_markup=keyboard)

@dp.callback_query_handler(text="back")
async def start_comms(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Информация о нас", callback_data="mainInfo"),
        types.InlineKeyboardButton(text="Продукты компании", callback_data="goods"),
        types.InlineKeyboardButton(text="Сотрудники и Контакты", callback_data="Contacts"),
        types.InlineKeyboardButton(text="Обучение должности", callback_data="job_feats")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Добро пожаловать в Nerv!; ПОЗЖЕ ЗАМЕНИТЬ НА ИНФ ИЗ БД ", reply_markup=keyboard)

@dp.callback_query_handler(text="mainInfo")
async def main_info(call: types.CallbackQuery):

    buttons = [
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.answer("ВВЕДИТЕ ИНФОРМАЦИЮ О КОМПАНИИ", reply_markup=keyboard)


@dp.callback_query_handler(text="goods")
async def main_goods(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="Good1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.answer("ВВЕСТИ ИНФ О ЕВА00", reply_markup=keyboard)

@dp.callback_query_handler(text="Good1")
async  def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="Good2"),
        types.InlineKeyboardButton(text="Назад", callback_data="Good1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.answer("ВВЕСТИ ИНФ О ЕВА01", reply_markup=keyboard)

@dp.callback_query_handler(text="Good2")
async  def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="Good3"),
        types.InlineKeyboardButton(text="Назад", callback_data="Good2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.answer("ВВЕСТИ ИНФ О ЕВА04", reply_markup=keyboard)



# @dp.callback_query_handler(text="+1.1")
# async def text_plus1(call: types.CallbackQuery, floor=floor):
#     floor = 2
#     buttons = [
#         types.InlineKeyboardButton(text="-1", callback_data="-1.2"),
#         types.InlineKeyboardButton(text="+1", callback_data="+1.2"),
#         types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish2")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     await call.message.edit_text("Этаж "+ str(floor), reply_markup=keyboard)
#
# @dp.callback_query_handler(text="+1.2")
# async def text_plus1(call: types.CallbackQuery, floor=floor):
#     floor = 3
#     buttons = [
#         types.InlineKeyboardButton(text="-1", callback_data="-1.3"),
#         types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish3")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     await call.message.edit_text("Этаж "+ str(floor), reply_markup=keyboard)
#

#
# @dp.callback_query_handler(text="-1.1")
# async def text_plus1(call: types.CallbackQuery, floor=floor):
#     floor = 0
#     buttons = [
#         types.InlineKeyboardButton(text="-1", callback_data="-1"),
#         types.InlineKeyboardButton(text="+1", callback_data="+1"),
#         types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish0")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     # await call.message.edit_media()
#     await call.message.edit_text(f"Этаж + {str(floor)}", reply_markup=keyboard)
#
# @dp.callback_query_handler(text="-1.2")
#
# async def text_plus1(call: types.CallbackQuery, floor=floor):
#     floor = 1
#     buttons = [
#         types.InlineKeyboardButton(text="-1", callback_data="-1.1"),
#         types.InlineKeyboardButton(text="+1", callback_data="+1.1"),
#         types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish1")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     await call.message.edit_text(f"Этаж + {str(floor)}", reply_markup=keyboard)
#
# @dp.callback_query_handler(text="-1.3")
# async def text_plus1 (call: types.CallbackQuery, floor=floor):
#     floor = 2
#     buttons = [
#         types.InlineKeyboardButton(text="-1", callback_data="-1.2"),
#         types.InlineKeyboardButton(text="+1", callback_data="+1.2"),
#         types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish2")
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     await call.message.edit_text("Этаж "+ str(floor), reply_markup=keyboard)
#




# @dp.callback_query_handler(text="+1")
# async def callbacks_lvl(call: types.CallbackQuery, userLvl=userLvl, callback=None):
#     if userLvl > 0:
#         await callback.message.delete()
#         keyboard = types.InlineKeyboardMarkup(row_width=2)
#         keyboard.add(*buttons)
#         if userLvl < 3:
#             userLvl = + 1
#         await call.message.edit_text(text=("Этаж " + str(userLvl)), reply_markup=keyboard)
#     else:
#         keyboard = types.InlineKeyboardMarkup(row_width=2)
#         keyboard.add(*buttons)
#         if userLvl < 3:
#             userLvl = + 1
#         await call.message.edit_text(text=("Этаж " + str(userLvl)), reply_markup=keyboard)
# @dp.callback_query_handler(text="+1")
# async def callbacks_lvl(call: types.CallbackQuery, userLvl=userLvl):
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     if userLvl < 3:
#         userLvl = + 1
#     await call.message.edit_text(text=("Этаж " + str(userLvl)), reply_markup=keyboard)
#
# @dp.callback_query_handler(text="-1")
# async def callbacks_lvl(call: types.CallbackQuery, userLvl=userLvl):
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     keyboard.add(*buttons)
#     if userLvl > 0:
#         userLvl =- 1


    # await call.message.edit_text(text=("Этаж " + str(userLvl)), reply_markup=keyboard)


# @dp.callback_query_handler(text="num_finish")
# async def callbacks_lvl(call: types.CallbackQuery):




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
