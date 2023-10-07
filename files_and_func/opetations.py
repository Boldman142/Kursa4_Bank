import json
import os


# "..", "start_data", "operations.json"
# "C:/Users/User/PycharmProjects/Kursa4_Bank/start_data/operations.json"
def load_data(path):
    """Функция достает файлы о последних операциях из json файла и выдает их"""
    #path = os.path.join("..", "start_data", "operations.json")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data
