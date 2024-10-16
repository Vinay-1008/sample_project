import requests

from Config.apis import ADD_OBJECT, LIST_OF_ALL_OBJECTS, UPDATE_OBJECT, DELETE_OBJECT


def get_all_objects():
    response = requests.get(LIST_OF_ALL_OBJECTS)
    if response.status_code == 200:
        return response.json()


def add_object(name, year, price, cpu_model, hard_disk_size):
    body = {
        "name": name,
        "data": {
            "year": year,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": hard_disk_size
        }
    }
    response = requests.post(ADD_OBJECT, json=body)
    if response.status_code == 200:
        return response.json()

def update_object(name, year, price, cpu_model, hard_disk_size, color):
    body = {
       "name": name,
       "data": {
          "year": year,
          "price": price,
          "CPU model": cpu_model,
          "Hard disk size": hard_disk_size,
          "color": color
       }
    }
    response = requests.put(UPDATE_OBJECT, json = body)
    if response.status_code != 200:
      print(f"Update object failed to update with the error {response.json()['error']}")
    return response.json()

def delete_object():
    response = requests.delete(DELETE_OBJECT)
    if response.status_code != 200:
        print(f"Delete object failed to delete with the error {response.json()['error']}")
    return response.json()

def test_sample_test_4():
    assert True

def test_sample_test_5():
    assert True
import pytest


def test_verify_name(input_name):
    assert input_name == "sreenu"

