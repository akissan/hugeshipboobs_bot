import asyncio
import json
import logging
from math import floor
from random import randint, random
import sys
from os import getenv
from typing import cast

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import F

from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN", "")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

krutki = {}

with open("gallery.json", "r", encoding="utf-8") as f:
    ships = json.load(f)

rarityList: dict[str, dict[str, dict[str, str]]] = ships
# shipList: dict[str, dict] =

# shipList = "\n".join(ships.keys())  # type: ignore
# shipTitles = ships.keys()  # type: ignore
# print(shipTitles)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """
    /start
    """

    kb = [
        [KeyboardButton(text="Ролльнуть корабледевочку")],
        [KeyboardButton(text="Фулл")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)

    await message.answer("Что зароллить?", reply_markup=keyboard)

@dp.message(F.text.lower() == "фулл")
async def full(message: Message):



@dp.message()
async def onAnyMessage(message: Message):
    """
    Ответ на любое сообщение
    """
    rarity = randint(2, 6)

    ships = rarityList[str(rarity)]
    shipCount = len(ships)

    roll = randint(0, shipCount - 1)

    shipName = list(ships.keys())[roll]

    await message.reply_photo(
        photo=ships[shipName]["src"],
        caption=f"{'⭐'*rarity:>6} {shipName}",
    )


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
