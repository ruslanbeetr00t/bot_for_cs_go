from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from setting import API, user_agent
from endopoint import items_url
from setings import TOKEN
import requests
import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    while True:
        await asyncio.sleep(10)
        payload = {'key': API}
        response = requests.get(url=items_url, headers=user_agent, params=payload, timeout=2)
        if response.status_code == 200:
            for status_item_info in response.json()["items"]:
                if status_item_info["status"] == "2":
                    await message.answer(f'SOLD!!!\nThis item user:- {status_item_info}')
                elif status_item_info["status"] == "4":
                    await message.answer(f'GET!!!\nThis item:-{status_item_info}')
                elif status_item_info["status"] == "3":
                    await message.answer(f'WAIT!!\nMaybe buy this item:- {status_item_info}')
                    """Для перевірки можна розкоментувати"""
                # elif status_item_info["status"] == "1":
                #     await message.answer(f'ADD!!\nThis item:- {status_item_info}')
            # await message.answer(response.json()["items"])


if __name__ == '__main__':
    executor.start_polling(dp)


"""
    status = 1 — Вещь выставлена на продажу.
    status = 2 — Вы продали вещь и должны ее передать боту.
    status = 3 — Ожидание передачи боту купленной вами вещи от продавца.
    status = 4 — Вы можете забрать купленную вещь.
"""
