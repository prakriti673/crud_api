# Third party app which will interact with the api at the frontend
import requests
import json

URL=" http://127.0.0.1:8000/studentapi/"

# If user asks for data with a particular id, he gets that field with id
# If id is not specified, he gets data of all students
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    r = requests.get(url=URL, data = json_data)
    data = r.json()
    print(data)

def post_data():
    # currently python data
    data = {
        'name':'Ravi',
        'roll': 105,
        'city': 'Ramgarh',
    }
    # flow-->
    # python data->json->to the api
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

def update_data():
    # currently python data
    data = {
        'id': 3,
        'name':'Suman',
    }
    # flow-->
    # python data->json->to the api
    json_data = json.dumps(data)

    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

def delete_data():
    data = {
        'id':4,
    }
    json_data = json.dumps(data)

    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)


delete_data()