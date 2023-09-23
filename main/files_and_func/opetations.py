import json
import os


def load_data():
    """Функция достает файлы о последних операциях из json файла и выдает их"""
    path = os.path.join("../../data/operations.json")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data
