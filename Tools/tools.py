from typing import Callable
import Objects.Transaction
import os
import pickle

saved_data_file = "/Users/josh/Code/budget/SavedData/.picklejar"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_user_input(prompt: str, valid_responses: [str], fun: Callable = None):
    response = None
    while response not in valid_responses:
        response = input(prompt)
        if fun is not None:
            try:
                response = fun(response)
            except:
                response = None
    return response

def serialize(data: [Objects.Transaction.Transaction]):
    data += deserialize()
    with open(saved_data_file, "wb") as f:
        pickler = pickle.Pickler(f)
        pickler.dump(data)

def deserialize() -> [Objects.Transaction.Transaction]:
    data = []
    if os.path.isfile(saved_data_file):
        with open(saved_data_file, "rb") as f:
            unpickler = pickle.Unpickler(f)
            data = unpickler.load()
        os.remove(saved_data_file)
    return data
