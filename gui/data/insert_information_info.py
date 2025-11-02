from sqlalchemy import create_engine, text

def insert_information_info(s, data):
                #вытащить и вставить
        query ="""
        INSERT INTO information(TypeS_id, object, sCount, sCaseCount, year)
        VALUES(:typ, :obj, :sC, :sCC, :y)
        """

        s.execute(text(query), {
                "typ": data['TypeS_id'],
                "obj": data['object'],
                "sC": data['sCount'],
                "sCC": data['sCaseCount'],
                "y": data['year']
            })
            
            
            #потверждаем
        s.commit()