import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile, CallbackQuery, InputMedia
from aiogram.utils.exceptions import BotBlocked
from random import randint
import aiogram.utils.markdown as fmt

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

bot = Bot(token="5854619199:AAFO2U5yfHrOm6_9wBZTfudLf_4dgkGizoM")   # Объект бота
dp = Dispatcher(bot)    # Диспетчер для бота
logging.basicConfig(level=logging.INFO)     # Включаем логирование, чтобы не пропустить важные сообщения
link = "https://sun1-86.userapi.com/impg/MXEUzx2_M5OB-VpY2A_d4uzPi0tDR37QW06UTg/UQbgMS-cy1U.jpg?size=1278x1080&quality=95&sign=d563a4a8badbe3cc89cce20572f6558a&type=album"
@dp.message_handler(commands="start")
async def start_comms(message: types.Message):
    await message.reply("Тестовые команды:\n/test1\n/test2\n/test4\n/block\n/answer\n/reply\n/dice\n/inline_url\n/random")

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Hello, *world*\!", parse_mode="MarkdownV2")

@dp.message_handler(commands="test2")
async def cmd_test2(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
            fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
            fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")

# @dp.message_handler()
# async def any_text_message(message: types.Message):
#     await message.answer(message.text)
#     await message.answer(message.md_text)
#     await message.answer(message.html_text)
#     # Дополняем исходный текст:
#     await message.answer(
#         f"<u>Ваш текст</u>:\n\n{message.html_text}", parse_mode="HTML"
#     )

@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")

@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')

@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

# @dp.message_handler(commands="Dice")
# async def cmd_dice(message: types.Message):
#     await message.bot.send_dice(-100123456789, emoji="🎲")

# @dp.message_handler()
# async def any_text_message2(message: types.Message):
#     await message.answer(f"Привет, <b>{fmt.quote_html(message.text)}</b>", parse_mode=types.ParseMode.HTML)
#     # А можно и так:
#     await message.answer(fmt.text("Привет,", fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)

@dp.message_handler(commands="test4")
async def with_hidden_link(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    buttons = ["С пюрешкой", "Без пюрешки"]
    keyboard.add(*buttons)
    await message.answer(
        f"{fmt.hide_link(link)}Паблик Джесси Пинкмант Интерпрайзед представляет:\n"
        f"-Say my name\n-Heisenberg\n-You are god damn right", reply_markup=keyboard,
        parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="С пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!"),
    reply_markup = types.ReplyKeyboardRemove()


@dp.message_handler(text="Без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!"),
    reply_markup = types.ReplyKeyboardRemove()

@dp.message_handler(commands="inline_url")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # Если нужно в ряд, row_widht = 3
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)

@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(randint(1, 10))),
    # await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)     # Строка чтобы около кнопки не было маленьких часиков

    @dp.message_handler(commands=["photo"])
    async def photo(message: types.Message):
        file_path = "files/foods/borsch.jpg"
        reply_markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(text="I want a new photo!", callback_data="update_photo")
        )
        file = InputFile(file_path)

        await bot.send_photo(
            message.chat.id,
            photo=file,
            reply_markup=reply_markup,
            caption="Test caption!",
        )

    @dp.callback_query_handler(text="update_photo")
    async def photo_update(query: CallbackQuery):
        file_path = "files/foods/pelmeni.png"
        reply_markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(text="Updated button", callback_data="dont_click_me")
        )
        file = InputMedia(media=InputFile(file_path), caption="Updated caption :)")

        await query.message.edit_media(file, reply_markup=reply_markup)




@dp.message_handler(commands="sss")
async def but1(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="push me", callback_data="button_pushed"))
    await message.answer("нажмите на кнопку", reply_markup=keyboard)

@dp.callback_query_handler(text="button_pushed")
async def editlastmsg(call: types.CallbackQuery):
    await call.message.edit_text("324678")
















if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)