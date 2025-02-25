import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()  # await дозволяє викликати coroutine (асинхронні функції)
    # # та інші об'єкти, які підтримують асинхронні операції
    bot = Bot(token='7582065547:AAF0AgoqtnVsLSkah0zZAwuuAJPCvT50cPU')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот вимкнен...')
