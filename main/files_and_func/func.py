from opetations import load_data
import time


def get_data():
    """Функция, которая выдает список операций, без пустых словарей и отсортированный по дате,
    а также добавляет ключ 'from' в те словари, где его нет"""
    operation_list = []
    operations = load_data()
    for pay in operations:
        if not pay == {}:
            if not "from" in pay:
                pay["from"] = None
            operation_list.append(pay)
    return list(sorted(operation_list, key=lambda x: time.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f')))


def complit_operation():
    """Функция отсортировывающая выполненные и не выполненные операции, на выходе только выполненные"""
    all_operation = get_data()
    comp = []
    for unit in all_operation:
        if unit["state"] == "EXECUTED":
            comp.append(unit)
    return comp


def show_latest_transaction(how):
    list_operation = complit_operation()
    for i in range(0, how):
        action = Operation(list_operation[i])
        message = f"""{action.message_date()} {action.message_who()}
{action.message_from()} -> {action.message_to()}
{action.message_how_many()} {action.message_currency()}\n"""
        print(message)


class Operation:
    def __init__(self, dic):
        self.date = dic["date"]
        self.whom = dic["description"]
        self.from_ = dic["from"]
        self.to = dic["to"]
        self.how_many = dic["operationAmount"]["amount"]
        self.currency = dic["operationAmount"]["currency"]["name"]

    def __repr__(self):
        return """Поля:
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
        .message_to - на какой счет осуществлен перевод, указываются его последние 4 цифры
        .message_how_many - какая сумма была переведена
        .message_currency - в какой валюте был перевод"""

    def message_date(self):
        """Метод возвращающий дату операции в необходимом формате"""
        date = self.date[:10].split("-")[::-1]
        return ".".join(date)

    def message_who(self):
        """Возвращает назначение перевода"""
        return self.whom

    def message_from(self):
        """Функция 'шифрующая' номер откуда совершен перевод звездочками, и разделяет номер
        на блоки по 4 цифры. На вывод идет сообщение с этим номером и указанием карты.
        Если в словаре об операции нет ключа 'From' выводит 'Неизвестно'"""
        if self.from_ is None:
            return "Неизвестно"
        text = self.from_.split(" ")
        num_from = list(str(text.pop(-1)))
        for number in range(6, len(num_from) - 4):
            del num_from[number]
            num_from.insert(number, "*")
        for num in range(len(num_from)):
            if num in [4, 9, 14, 19, 24, 29]:
                num_from.insert(num, " ")
        secret_num = "".join(num_from)
        text.append(secret_num)
        return " ".join(text)

    def message_to(self):
        """Функция возвращает название карты откуда совершен перевод, и его последние 4 цифры"""
        text = self.to.split(" ")
        num_to = list(str(text.pop(-1)))[-4:]
        [num_to.insert(0, "*") for i in range(0, 2)]
        secret_num_to = "".join(num_to)
        text.append(secret_num_to)
        return " ".join(text)

    def message_how_many(self):
        """Возвращает сумму перевода"""
        return self.how_many

    def message_currency(self):
        """Возвращает значение валюты, в которой был осуществлен перевод"""
        return self.currency
