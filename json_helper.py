import json
import os
import pickle

file_path = '/Users/robert/Desktop/PythonProjects/PyFun9/data/super_smash_bros/link.json'

def read_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        return data

read_json(file_path)


def read_all_json_files():
    json_list = []
    json_list.append(read_json(file_path))
    return json_list

read_all_json_files()



def write_pickle():
    pass

def load_pickle():
    pass
