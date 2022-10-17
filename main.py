from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()


inventory = {1:{
                 "name":"milk",
                'price':'3,99',
                'brand':'regular'
    }}

@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory

@app.get("/get-by-name/{item_od}")
def get_item(*item_id:int,test:int, name :Optional[str]=None):
    for item_id in inventory :
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return{'Data':'Not found'}
    

@app.get("/")
def home():
    return {"data": "test"}


@app.get("/about")
def about():
    return {"data": "about"}