from fastapi import FastAPI
from typing import Union,Optional
from pydantic import BaseModel

app=FastAPI()

class item(BaseModel):
    item_id:int
    q:Optional[str]=None

@app.get("/")
def read_root():
    return {"Hello" : "world"}

@app.get("/item/{item_id}")
def read_item(item_id:int,q:Union[str,None]=None):
    return {"item_id":item_id,"q":q}
    
@app.post("/item/{item_id}")
def read_item(item_id:int,q:str):
    return {"item_id":item_id,"q":q}
    
