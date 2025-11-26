import random
from colorama import init, Fore

init(autoreset=True)

secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100, попробуй угадать")

while True:
    guess_str = input("Введи число: ")

    if not guess_str.isdigit():
        print(Fore.RED + "Введите целое положительное число!")
        continue

    guess = int(guess_str)
    attempts += 1

    if guess > secret_number:
        print(Fore.RED + "Слишком много!")
    elif guess < secret_number:
        print(Fore.BLUE + "Слишком мало!")
    else:
        print(Fore.GREEN + "Поздравляю! Вы угадали число!")
        print(f"Количество попыток: {attempts}")
        break



import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    current_time = time.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)





import requests

url = input("Введите URL (например, https://ya.ru): ")

try:
    response = requests.get(url, timeout=5)

    if 200 <= response.status_code < 400:
        print(f" Сайт доступен. Код ответа: {response.status_code}")
    else:
        print(f" Сайт недоступен. Код: {response.status_code}")

except requests.exceptions.ConnectionError:
    print(" Ошибка подключения: невозможно установить соединение.")
except requests.exceptions.Timeout:
    print(" Ошибка: превышено время ожидания ответа.")
except Exception as e:
    print(f" Непредвиденная ошибка: {e}")