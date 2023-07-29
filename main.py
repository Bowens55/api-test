from fastapi import FastAPI
#from core.config import settings

app = FastAPI()#title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION) # wonder how this will work with docker

inventory = {
    1: {
        "name": "Milk",
        "price": "2.99",
    },
    2: {
        "name": "Eggs",
        "price": "8.00",
    }
}

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}

@app.get("/hi-drew")
def hello_drew():
    return {"msg": "Hi Drew"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for id in inventory:
       if inventory[id]["name"] == name:
           return inventory[id]



