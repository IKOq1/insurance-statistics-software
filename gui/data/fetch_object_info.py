from sqlalchemy import text
from sqlalchemy.orm import Session

def fetch_object_info(s: Session):
            query = """
            SELECT DISTINCT object
            FROM information
            """
            rows = s.execute(text(query))
            return rows

        
            #разблокируем сигналы после циклирования