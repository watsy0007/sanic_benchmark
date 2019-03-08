import asyncio
import sqlalchemy as sa
from aiomysql.sa import create_engine
from sqlalchemy.ext.automap import automap_base

metabase = sa.MetaData()

tbl_alternative = sa.Table('index_third_alternative', 
                    metabase, 
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('value', sa.Integer),
                    sa.Column('value_classification', sa.VARCHAR),
                    sa.Column('timestamp', sa.Integer)
                    )

configs = {}

async def get_engine(ev_loop):
    if ev_loop not in configs:
        configs[ev_loop] = await create_engine(user='root', db='quantum_tunnel',host='0.0.0.0', port=3306, password='my-secret-pw', loop=ev_loop)
    return configs[ev_loop]

async def query_method(ev_loop, func):
    engine = await get_engine(ev_loop)
    async with engine.acquire() as conn:
        return await func(conn)


async def query_alternative(ev_loop):
    async def _query(conn):
        return await conn.execute(tbl_alternative.select())
    r = await query_method(ev_loop, _query)
    return [{'id': row.id, 
             'value': row.value, 
             'value_classification': row.value_classification, 
             'timestamp': row.timestamp} 
             for row in (await r.fetchall())]
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(query_alternative(loop))

