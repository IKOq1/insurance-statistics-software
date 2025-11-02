from sqlalchemy import create_engine, text

def delete_information_info(s, data):
    query = """
                DELETE FROM information
                WHERE id =:id
                """
    s.execute(text(query), {
                    "id" : data.id
                })

    s.commit()