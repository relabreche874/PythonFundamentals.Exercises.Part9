import json
import os
import pickle

file_path = '/Users/robert/Desktop/PythonProjects/PyFun9/data/super_smash_bros/link.json'

def read_json(file_path):
    with open(file_path) as file:
        new_data = json.load(file)
        return new_data

read_json(file_path)


def read_all_json_files():
    json_list = []
    json_list.append(read_json(file_path))
    return json_list

read_all_json_files()

data = ['Shy Guy', 'Isabelle', 'Bowzer']

def write_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return file
