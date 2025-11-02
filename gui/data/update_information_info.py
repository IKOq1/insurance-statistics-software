from sqlalchemy import create_engine, text

def update_information_info(s, data, init_data):
    query = """
            UPDATE information
            SET year = :y, object = :obj, sCount =:sC, sCaseCount = :sCC
            WHERE id = :id
            """
    s.execute(text(query),{
            "y":data['year'],
            "obj":data['object'],
            "sC":data['sCount'],
            "sCC":data['sCaseCount'],
            "id": init_data.id    
        })
    s.commit()