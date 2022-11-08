import requests
import json

# user


def InsertApi(username, password):
    result = requests.put(
        'http://127.0.0.1:4000/InsertDataUser/?username={0}&password={1}'.format(username, password))
    return result.json()


def check_credo_API(username, password):
    result = requests.get(
        'http://127.0.0.1:4000/CheckUser/?username={0}&password={1}'.format(username, password))
    return result.json()


# food
def getter_all_api(username):
    result = requests.get(
        'http://127.0.0.1:4000/GetList/?username={0}'.format(username))
    return result.json()


def update_api(newItem, oldItem, UserData):
    result = requests.put(
        'http://127.0.0.1:4000/UpdateItem/?olditem={0}&newItem={1}&username={2}'.format(oldItem, newItem, UserData))
    return result.json()


def delete_api(food, username):
    result = requests.delete(
        'http://127.0.0.1:4000/DeleteItem/?item={0}&username={1}'.format(food, username))
    print(result)
    return result.json()


def insert_apio(username, food):
    result = requests.post(
        'http://127.0.0.1:4000/NewItem/?username={0}&new_food={1}'.format(username, food))
    return result.json()
