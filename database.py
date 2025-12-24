# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    return create_engine(DATABASE_URL)


engine = get_connection()


##get jobs from db
def get_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        print(type(result_all))

    dic_all = {value for index, value in enumerate(result_all)}
    print(dic_all)
    return dic_all
