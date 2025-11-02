import sys
import aiosqlite
import logging
from pathlib import Path

from DbTg import dbForTg
from DbTg.dbForTg import INSERT_Information  # Корректный абсолютный импорт





DB_PATH = Path(__file__).parent.parent / 'MainDB.db'

async def save_information(data:dict):
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            TypeS_id = int(data.get('TypeS_id', 0))
            sCount = int(data.get('sCount', 0))
            sCaseCount = int(data.get('sCaseCount',0))
            year = int(data.get('year', 0))

            await db.execute(
                dbForTg.INSERT_Information,(
                    TypeS_id,
                    data.get('object'),
                    sCount,
                    sCaseCount,
                    year
                )
            )
            await db.commit()
            logging.info(f'Data successfully')
            return True
        

    except ValueError as e:
        logging.error(f'Data error conversion{e}')
    except aiosqlite.Error as e:
        logging.error(f'error db{e}')
    except Exception as e:
        logging.error(f'unexpected error')