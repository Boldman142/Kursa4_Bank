import json
import os


def load_data(path):
    """Функция достает файлы о последних операциях из json файла и выдает их"""

    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data
