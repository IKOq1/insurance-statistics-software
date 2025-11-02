from sqlalchemy import text
from sqlalchemy.orm import Session


def typeS_information_info(s: Session):
            query = """
            SELECT * 
            FROM TypeS
            """
            rows = s.execute(text(query))
            return rows