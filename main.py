import asyncio
from aiogram import Bot, Dispatcher

from handlers import router


async def main():
    bot = Bot(token='7130979300:AAHLzOh5RIzqLS7SZJr_nQXMr1VvOHu7Yx0')
    dsp = Dispatcher()
    dsp.include_router(router)
    await dsp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отключен')
