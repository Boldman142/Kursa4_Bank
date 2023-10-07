from files_and_func.opetations import load_data
import os


def test_load_data():
    path = os.path.join("operations_2.json")
    assert isinstance(load_data(path), list)

    # assert load_data(os.path.join("start_data", "operations.json")) == get_all_operations
    # get_all_operations
