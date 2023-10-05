import pytest
import json
import os

from files_and_func.opetations import load_data


@pytest.fixture
def get_all_operations():
    path = os.path.join("..", "start_data", "operations.json")
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def test_load_data(get_all_operations):
    assert load_data() == get_all_operations
