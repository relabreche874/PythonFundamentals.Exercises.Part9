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
    with open('super_smash_characters.pickle', 'wb') as file:
        pickle.dump(data, open(file, 'wb'))

write_pickle(data, file_path)

def load_pickle(file_path):
    return pickle.load(file_path, 'rb')
