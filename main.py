import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI

from pydantic import BaseModel
from mylib.bot import scrape

app = FastAPI()


class Wiki(BaseModel):
    name: str


@app.post("/wiki")
async def wiki(wiki: Wiki):
    result = scrape(name=wiki.name)
    payload = {"Wiki page": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/")
async def root():
    return {"Message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
