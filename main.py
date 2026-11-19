import asyncio
import logging
from aiogram import F
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command


BOT_TOKEN = "8656395687:AAHCRhuFzi_TRvvYvQdvuRUI_1pQEbOtE4E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name} я твой бот!"
  )
    print(f"Пользователь {message.from_user.full_name} написал команду /start!")
    

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "/start - команда для запуска\n"
        "/help - список команд"
    )


@dp.message(F.text.lower() == "группа")
async def cmd_group(message: Message):
    await message.answer("Твоя группа 71-1!")

    

@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")


    


async def main():
    await dp.start_polling(bot)


if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

echo "# group-71-1-month3" >> README.md
https://github.com/5aguma/group-71-1-month3.git