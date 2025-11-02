import asyncio
import logging

import sys
from pathlib import Path
from aiogram import Dispatcher, Bot

# Добавляем корень проекта (EEE/) в пути Python
sys.path.append(str(Path(__file__).parent.parent))

from app.handlers import router
from config_reader import BOT_TOKEN





bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def on_start():
    from DbTg.dbAsync import DB_PATH
    if not DB_PATH.exists():
        logging.error(f'File BD not fount {DB_PATH}')
    else:
        logging.info('BD succeffully connect')

async def main():
    print(Path(__file__).parent.parent.parent)
    await on_start()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    #чтобы не вылазала класная штука в консоле
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')
