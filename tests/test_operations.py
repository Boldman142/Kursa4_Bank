from files_and_func.opetations import load_data


def test_load_data(get_all_operations):
    assert load_data() == get_all_operations
