import logging  # тг логгинг в бота
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMedia
import sqlite3
from sqlite3 import Error




conn = None
try:
        conn = sqlite3.connect(".\zxcasuka (1).db")
        cursor = conn.cursor()
        print("Connection to SQLite DB successful")#подключение к бд
        overallinf = cursor.execute(""" SELECT user_info FROM 'recrd' """) #получение информации из каждой строки бд для дальнейшего использования
        overallinf = overallinf.fetchall()
        overallname = cursor.execute("""SELECT name FROM 'recrd' """)
        overallname = overallname.fetchall()
        overallid = cursor.execute("""SELECT id FROM 'recrd' """)
        overallid = overallid.fetchall()
except Error as e:
    print(f"The error '{e}' occurred")#при ошибке подключения или получ. инф из каждой строки бд

conn = None #после всех действий отключаемся от бд



g10 = str(*overallname[5]) + f"\n\n" + str(*overallinf[5])
g1 = str(*overallname[5]) + f"\n\n" + str(*overallinf[5])
g2 = str(*overallname[6]) + f"\n\n" + str(*overallinf[6])
g3 = str(*overallname[7]) + f"\n\n" + str(*overallinf[7])
g4 = str(*overallname[8]) + f"\n\n" + str(*overallinf[8])
e1 = str(*overallname[0]) + f"\n\n" + str(*overallinf[0])
e2 = str(*overallname[1]) + f"\n\n" + str(*overallinf[1])
e3 = str(*overallname[2]) + f"\n\n" + str(*overallinf[2])
e4 = str(*overallname[3]) + f"\n\n" + str(*overallinf[3])
e5 = str(*overallname[4]) + f"\n\n" + str(*overallinf[4])
jobinf = str(*overallname[10]) + f"\n\n" + str(*overallinf[10])
# структуризация будущего текста. необязательно, но для единого стиля неплохо
nervlogo = InputMedia(type="photo", media="https://sun9-49.userapi.com/impg/MMepAmaUCdPhDIC_y-2JP6RspQB_xL5vHWpGQg/plc1NVv_A28.jpg?size=1600x1600&quality=95&sign=5698d100477cdb25d13c33019677b6db&type=album")
eva00 = InputMedia(type="photo", media="https://sun9-21.userapi.com/impg/v8R4UZa6EJT66ZMP2xkzxTOqCpzSxb1tYI5MyQ/612HPwqWsWw.jpg?size=768x576&quality=95&sign=69fc2b0e75ef5e8b6203cf50768f4d72&type=album")
eva01 = InputMedia(type="photo", media="https://sun9-15.userapi.com/impg/hkP1tLut5EFwVXVy-1VB5GVk_oEVCRB6S7vbww/vQDe71d44N0.jpg?size=1440x1080&quality=95&sign=f5e5508853deb0c22ea0c6221fa080f8&type=album")
eva02 = InputMedia(type="photo", media="https://sun9-25.userapi.com/impg/VDTwzaCVoV8RHhjbBNwmF6pP0MrGW6J72CJjUw/aRUZVHcCI_s.jpg?size=640x480&quality=95&sign=bbc63b99be9bdc2c6651604289fe4191&type=album")
eva03 = InputMedia(type="photo", media="https://sun9-48.userapi.com/impg/lt9eyp9QfyL1GkBKMw7NN_h3ubmDuYVhHF7epQ/bfOO-pGjwGM.jpg?size=875x980&quality=95&sign=e861ceb1bfe09663b5e34f9001c34ef7&type=album")
gendo = InputMedia(type="photo", media="https://sun9-20.userapi.com/impg/hKETV5zbnQCmXhpQVVtx526uKaFY9VM7fAH3Kw/DjDRPLNE05E.jpg?size=1600x2000&quality=95&sign=bb347a40ca95400f0f75e48eb20aecbb&type=album")
misato = InputMedia(type="photo", media="https://sun9-24.userapi.com/impg/hXpgzWLbLiqxU0MUbhi2C4HQUWTDaF6Q0MuiQA/6Uax8lLkC-o.jpg?size=400x393&quality=95&sign=08df36e2a682a1a642c5a8f59779c7ef&type=album")
mayaibuki = InputMedia(type="photo", media="https://sun9-79.userapi.com/impg/jgEhpKhbByfROHUSVcfnbJVtgQolflfGSucwgw/QRrFhQegNLQ.jpg?size=1200x675&quality=95&sign=658455c9ee76cfd3130e423132c1f174&type=album")
ritcuko = InputMedia(type="photo", media="https://sun9-14.userapi.com/impg/QrDG50Dbg_rD7MTcGanA2xubTUAbzGxQMNlK0Q/6Botdvf1Gos.jpg?size=1242x940&quality=95&sign=18a8ad12c0fdb31f87f0eebe325b83e1&type=album")
makoto = InputMedia(type="photo", media="https://sun9-33.userapi.com/impg/HNndrPpmqRRobAKrOVwAKNqjPeUiFvU9uI1xtA/hl8IbmOgsSg.jpg?size=225x350&quality=95&sign=f217ca844011e91f98ed1ae5c38b8163&type=album")
magi = InputMedia(type="photo", media="https://sun9-33.userapi.com/impg/_GeklEVDLUs2d_KcO9UST598vUbNudVcnht4Wg/G5oOHoKzaPE.jpg?size=1600x2000&quality=95&sign=35a8896009b9286110e67dbc50512623&type=album")
#Создание переменных отвечающие за изображения в сообщениях
bot = Bot(token="5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
#необходимые для бота значения

#объявляем каждую из функций (сообщений)
#Каждое сообщение является или овтетом на команду .messag_handler или ответом но нажаитие нкнопки .callback_query_handler
@dp.message_handler(commands="start")
async def start_comms(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="О нас", callback_data="mainInfo"),#callback_data будет триггером для будущих сообщений
        types.InlineKeyboardButton(text="Продукты", callback_data="goods"),
        types.InlineKeyboardButton(text="Сотрудники", callback_data="employees"),
        types.InlineKeyboardButton(text="Обучение должности", callback_data="job_feats")
    ]
    keyboard = types.InlineKeyboardMarkup() # Задаются кнопки, создавая картеж с инф. о самих кнопках
    keyboard.add(*buttons)
    await message.answer_photo(photo="https://sun9-49.userapi.com/impg/MMepAmaUCdPhDIC_y-2JP6RspQB_xL5vHWpGQg/plc1NVv_A28.jpg?size=1600x1600&quality=95&sign=5698d100477cdb25d13c33019677b6db&type=album", caption=f"Добро пожаловать в onboarding бота Nerv!\nВы можете ознакомиться с продукцией, вашими коллегами, общей инфорамцией о компании и дожлностными обязанностями.",parse_mode=types.ParseMode.HTML, reply_markup=keyboard)
# После отправки или имзменения каждого сообщения необходимо добавлять параметр replay_markup
# parse_mode отвечает за способ модификации текста(\n для пробела строк - HTML)

@dp.callback_query_handler(text="mainInfo")
async def main_info(call: types.CallbackQuery):

    buttons = [
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.edit_caption(*overallinf[9], reply_markup=keyboard)


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
    await call.message.edit_media(media=nervlogo, reply_markup=keyboard)# Если следующее сообщение подразумевает изменение картинки и текста, то делаем отдельно
    await call.message.edit_caption("Добро пожаловать в onboarding бота Nerv!\nВы можете ознакомиться с продукцией, вашими коллегами, общей инфорамцией о компании и дожлностными обязанностями.", parse_mode=types.ParseMode.HTML, reply_markup=keyboard)


@dp.callback_query_handler(text="goods")
async def main_goods(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="Good1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_media(eva00, reply_markup=keyboard)
    await call.message.edit_caption(g1, parse_mode=types.ParseMode.HTML, reply_markup=keyboard)


@dp.callback_query_handler(text="Good1")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="goods"),
        types.InlineKeyboardButton(text="Далее", callback_data="Good2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_media(eva01, reply_markup=keyboard)
    await call.message.edit_caption(g2, reply_markup=keyboard)


@dp.callback_query_handler(text="Good2")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="Good1"),
        types.InlineKeyboardButton(text="Далее", callback_data="Good3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_media(eva02, reply_markup=keyboard)
    await call.message.edit_caption(g3, reply_markup=keyboard)


@dp.callback_query_handler(text="Good3")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="Good2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_media(eva03, reply_markup=keyboard)
    await call.message.edit_caption(g4, reply_markup=keyboard)


@dp.callback_query_handler(text="employees")
async def main_goods(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Далее", callback_data="empl1"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_media(gendo, reply_markup=keyboard)
    await call.message.edit_caption(e1, reply_markup=keyboard)


@dp.callback_query_handler(text="empl1")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="employees"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl2"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_media(misato, reply_markup=keyboard)
    await call.message.edit_caption(e2, reply_markup=keyboard)


@dp.callback_query_handler(text="empl2")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl1"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_media(makoto, reply_markup=keyboard)
    await call.message.edit_caption(e3, reply_markup=keyboard)


@dp.callback_query_handler(text="empl3")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl2"),
        types.InlineKeyboardButton(text="Далее", callback_data="empl4"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_media(ritcuko, reply_markup=keyboard)
    await call.message.edit_caption(e4, reply_markup=keyboard)


@dp.callback_query_handler(text="empl4")
async def goods1(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data="empl3"),
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_media(mayaibuki, reply_markup=keyboard)
    await call.message.edit_caption(e5, reply_markup=keyboard)


@dp.callback_query_handler(text="job_feats")
async def jobfeats(call: types.CallbackQuery):

    buttons = [
        types.InlineKeyboardButton(text="Вернуться в меню", callback_data="back"),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await call.message.edit_media(magi, reply_markup=keyboard)
    await call.message.edit_caption(jobinf, reply_markup=keyboard)

#запускаем бота
if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)
