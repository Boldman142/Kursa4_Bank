from files_and_func.func import show_latest_transaction
import os

if __name__ == "__main__":
    how = int(input("Сколько последних операций хотите посмотреть? "))
    path = os.path.join("..", "start_data", "operations.json")
    show_latest_transaction(how, path)
