import json
import os


# "..", "start_data", "operations.json"

def load_data():
    """Функция достает файлы о последних операциях из json файла и выдает их"""
    # path = os.path.join()
    with open("C:/Users/User/PycharmProjects/Kursa4_Bank/start_data/operations.json", encoding='utf-8') as file:
        data = json.load(file)
    return data
