from sanic import Sanic
from sanic.response import json as r_json
from sync_models import query_alternative as sync_query
from async_model import query_alternative as async_query
import asyncio
app = Sanic()

@app.route('/async')
async def async_(request):
    r = await async_query(asyncio.get_event_loop())
    return r_json(r)

@app.route('/sync')
async def sync(request):
    r = sync_query(asyncio.get_event_loop())
    return r_json(r)

@app.route('/')
async def index(request):
    return r_json({'hello', 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)