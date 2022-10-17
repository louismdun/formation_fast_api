from fastapi import FastAPI
app = FastAPI()


inventory = {1:{
                 "name":"milk",
                'price':'3,99',
                'brand':'regular'
    }}

@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory
    

@app.get("/")
def home():
    return {"data": "test"}


@app.get("/about")
def about():
    return {"data": "about"}