import asyncio
from aiogram import Bot, Dispatcher, executor
from config import TOKEN

TOKEN = "1915822793:AAF0mM0TMZj4krXzZLy3NYctlOa-AaV9WfU"
my_id = 820502402

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id, text="hello yers")

@dp.message_handler()
async def echo(message):
    n = f"Hi Patrik: {message.text}"
    if message.text == "hello":
        await bot.send_message(chat_id=message.from_user.id, text="you are welcom")
    elif message.text == "Thank u":
        await bot.send_message(chat_id= message.from_user.id, text="can i help?")
    elif message.text == "with what":
        await bot.send_message(chat_id= message.from_user.id, text="with job")
    elif message.text == "cool":
        await bot.send_message(chat_id= message.from_user.id, text="Stay with me")
    else:
        await bot.send_message(chat_id=message.from_user.id, text= "i  dont understand")

if __name__ == "__main__":
    from dispacher import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)