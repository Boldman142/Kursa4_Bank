from files_and_func.func import *  # show_latest_transaction

how = int(input("Сколько последний операций хотите посмотреть? "))
full = input("Хотите посмотреть только завершенные операции? (Да/Нет) ").lower()
if full == "да":
    yep = True
else:
    yep = False
show_latest_transaction(how, yep)
