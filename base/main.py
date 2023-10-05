from files_and_func.func import show_latest_transaction

if __name__ == "__main__":
    how = int(input("Сколько последних операций хотите посмотреть? "))
    show_latest_transaction(how)
