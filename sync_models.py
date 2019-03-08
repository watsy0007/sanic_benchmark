from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("mysql+pymysql://root:my-secret-pw@0.0.0.0:3306/quantum_tunnel")

Base.prepare(engine, reflect = True)

Alternative = Base.classes.index_third_alternative

session = Session(engine)


def query_alternative(ev_loop):
    res = session.query(Alternative).all()
    return [{'id': row.id, 
             'value': row.value, 
             'value_classification': row.value_classification, 
             'timestamp': row.timestamp} 
             for row in res]


if __name__ == "__main__":
    query_alternative(None)    