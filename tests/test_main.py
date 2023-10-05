from base.main import *


def test_main():
    assert show_latest_transaction(1) == print("""13.01.2018 Перевод с карты на карту
Visa Classic 8906 17** **** 3215 -> Visa Platinum **8217
55985.82 USD""")
