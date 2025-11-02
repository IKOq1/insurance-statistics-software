from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

def fetch_information_info(s: Session, typeS_id, object_filter):
    query = """
            SELECT i.*, t.title as TypeS_title
            FROM information i
            LEFT JOIN TypeS t ON i.TypeS_id = t.id
            WHERE (:rid=0 OR TypeS_id = :rid)
                AND ( :obj IS NULL OR object = :obj)
            ORDER BY  year DESC
            """ 
    rows = s.execute(text(query), {
        "rid": typeS_id,
        "obj": object_filter
            })
    
    
    return rows 