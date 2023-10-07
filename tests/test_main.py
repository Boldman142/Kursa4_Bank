from base.main import *


def test_main():
    path_ = os.path.join("start_data", "operations.json")
    assert show_latest_transaction(1, path_) == print("""08.12.2019 Открытие вклада
Неизвестно -> Счет **5907
41096.24 USD""")
