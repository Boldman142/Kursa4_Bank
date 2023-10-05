import pytest

from files_and_func.func import *


@pytest.fixture
def get_dic():
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 35383033474447895560"
        }
    ]


@pytest.fixture
def answer():
    return ["""13.01.2018 Перевод с карты на карту
Visa Classic 8906 17** **** 3215 -> Visa Platinum **8217
55985.82 USD""",
            """21.01.2018 Перевод со счета на счет
Счет 3340 72** **** **** 7865 -> Счет **1215
96900.90 руб."""
            ]


@pytest.mark.parametrize("get,num", [("26.08.2019", 0), ("03.07.2019", 1)])
def test_class_operation_message_date(get_dic, get, num):
    test_operation_message_date = Operation(get_dic[num])
    assert test_operation_message_date.message_date() == get


@pytest.mark.parametrize("get_num,num", [("Maestro 1596 83** **** 5199", 0), ("Неизвестно", 1)])
def test_class_operation_message_from(get_dic, get_num, num):
    test_operation_message_from = Operation(get_dic[num])
    assert test_operation_message_from.message_from() == get_num


@pytest.mark.parametrize("get_num_1,num", [("Счет **9589", 0), ("Счет **5560", 1)])
def test_class_operation_message_to(get_dic, get_num_1, num):
    test_operation_message_to = Operation(get_dic[num])
    assert test_operation_message_to.message_to() == get_num_1


def test_repr(get_dic):
    assert repr(Operation(get_dic[1])) == """Поля:
        .date - дата операции
        .whom - описание перевода
        .from_ - откуда осуществлен перевод
        .to - куда осуществлен перевод
        .how_many - сумма перевода
        .currency - валюта перевода         
Методы:
        .message_date - дата операции в необходимом формате
        .message_who - назначение перевода
        .message_from - с какого счета осуществлена операция, номер указывается зашифрованным
        .message_to - на какой счет осуществлен перевод, указываются его последние 4 цифры"""


def test_message_who(get_dic):
    assert Operation(get_dic[0]).message_who() == "Перевод организации"


def test_show_latest_transaction(answer):
    assert show_latest_transaction(1) == print(answer[0])
    assert show_latest_transaction(2) == print(answer)
