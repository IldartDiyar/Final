import uvicorn
from Management.database import DatabaseM
from fastapi import FastAPI

managedb = DatabaseM()
app = FastAPI()


@app.get("/")
async def root():
    return True


# User sider
@app.put("/InsertDataUser/")
def InsertDataUser(username, password):
    db = managedb.add_new_User(username, password)
    return db


@app.get("/CheckUser/")
def CheckUser(username, password):
    db = managedb.get_by_pass(username, password)
    return db

# List side


@app.get("/GetList/")
def GetList(username):
    db = managedb.get_all_food(username)
    print(db)
    return db


@app.post("/NewItem/")
def NewItem(username, new_food):
    db = managedb.add_new(new_food, username)
    return db


@app.put("/UpdateItem/")
def UpdateItem(olditem, newItem, username):
    db = managedb.update(olditem, newItem, username)
    return db


@app.delete("/DeleteItem/")
def DeleteItem(username, item):
    db = managedb.delete(username, item)
    return db


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=4000)
