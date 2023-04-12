import logging
from aiogram import Bot, Dispatcher, executor, types
# import asyncio
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile, CallbackQuery, InputMedia
# from aiogram.utils.exceptions import BotBlocked
# from random import randint
# import aiogram.utils.markdown as fmt
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(".\zxcasuka.db")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection



bot = Bot(token="5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
floor = 0


@dp.message_handler(commands="start")
async def start_comms(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="О нас", callback_data="mainInfo"),
        types.InlineKeyboardButton(text="Продукты", callback_data="goods"),
        types.InlineKeyboardButton(text="Сотрудники", callback_data="employees"),
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
    await call.message.edit_text("ВВЕДИТЕ ИНФОРМАЦИЮ О КОМПАНИИ", reply_markup=keyboard)


@dp.callback_query_handler(text="back")
async def start_comms(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="О нас", callback_data="mainInfo"),
        types.InlineKeyboardButton(text="Продукты", callback_data="goods"),
        types.InlineKeyboardButton(text="Сотрудники", callback_data="employees"),
        types.InlineKeyboardButton(text="Обучение должности", callback_data="job_feats")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.edit_text("Добро пожаловать в Nerv!; ПОЗЖЕ ЗАМЕНИТЬ НА ИНФ ИЗ БД ", reply_markup=keyboard)




@dp.callback_query_handler(text="goods")
async def main_goods(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="Good1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ЕВА00", reply_markup=keyboard)

@dp.callback_query_handler(text="Good1")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="goods"),
        types.InlineKeyboardButton(text="Далее", callback_data="Good2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ЕВА01", reply_markup=keyboard)

@dp.callback_query_handler(text="Good2")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="Good1"),
        types.InlineKeyboardButton(text="Далее", callback_data="Good3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ЕВА02", reply_markup=keyboard)

@dp.callback_query_handler(text="Good3")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="Good2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ЕВА04", reply_markup=keyboard)


#
#

@dp.callback_query_handler(text="employees")
async def main_goods(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="empl1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ГЕНДО", reply_markup=keyboard)

@dp.callback_query_handler(text="empl1")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="employees"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О МИСАТО", reply_markup=keyboard)

@dp.callback_query_handler(text="empl2")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl1"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ПОМОШНИКЕ МИСАТО", reply_markup=keyboard)

@dp.callback_query_handler(text="empl3")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl2"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl4"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О РИТЦУКО", reply_markup=keyboard)

@dp.callback_query_handler(text="empl4")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ВАШЕЙ ПРОФЕССИИ", reply_markup=keyboard)

@dp.callback_query_handler(text="job_feats")
async def jobfeats(call: types.CallbackQuery):

    buttons = [
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.edit_text("ВВЕСТИ ИНФ О ВАШЕЙ ПРОФЕССИИ", reply_markup=keyboard)

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
    executor.start_polling(dp, skip_updates=True)
