import pytest
import json
import os


@pytest.fixture
def get_all_operations():
    path = os.path.join("..", "start_data", "operations.json")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data
