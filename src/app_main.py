from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hell() -> dict:
    return {'message': 'Hello'}
