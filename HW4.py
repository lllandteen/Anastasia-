
ROWS = 8
SEATS = 10


hall = [[0] * SEATS for _ in range(ROWS)]


prices = {
    1: 500, 2: 500, 3: 500,  
    4: 300, 5: 300, 6: 300,  
    7: 200, 8: 200           
}

sales_total = 0   
popular_rows = [0] * ROWS  


def show_hall():
    print("\nСхема зала:")
    print("     " + " ".join(f"{i:2d}" for i in range(1, SEATS + 1)))

    for i in range(ROWS):
        row_display = " ".join("[X]" if seat == 1 else "[0]" for seat in hall[i])
        print(f"Ряд {i + 1} {row_display} {prices[i + 1]}₽")


def book_seats():
    global sales_total

    count = int(input("Сколько мест хотите забронировать? "))

    for _ in range(count):
        row = int(input("Ряд: "))
        seat = int(input("Место: "))

        if row < 1 or row > ROWS or seat < 1 or seat > SEATS:
            print("Неверный номер места.")
            continue

        if hall[row - 1][seat - 1] == 1:
            print("Место уже занято.")
            continue

        price = prices[row]
        confirm = input(f"Цена: {price} руб. Подтвердить бронь? (да/нет): ")

        if confirm.lower() == "да":
            hall[row - 1][seat - 1] = 1
            sales_total += price
            popular_rows[row - 1] += 1
            print("Место забронировано!")
        else:
            print("Отмена.")


def cancel_booking():
    row = int(input("Ряд: "))
    seat = int(input("Место: "))

    if hall[row - 1][seat - 1] == 0:
        print("Место и так свободно.")
        return

    price = prices[row]
    confirm = input(f"Вернуть бронь места за {price} руб? (да/нет): ")

    if confirm.lower() == "да":
        hall[row - 1][seat - 1] = 0
        sales_total -= price
        popular_rows[row - 1] -= 1
        print("Бронь отменена.")
    else:
        print("Отмена операции.")


def show_stats():
    total = ROWS * SEATS
    occupied = sum(sum(row) for row in hall)
    free = total - occupied
    percent = (occupied / total) * 100
    popular = max(popular_rows)
    popular_row = popular_rows.index(popular) + 1 if popular > 0 else "-"

    print("\nСтатистика:")
    print(f"- Свободно: {free} мест")
    print(f"- Занято: {occupied} мест")
    print(f"- Заполненность: {percent:.2f}%")
    print(f"- Выручка: {sales_total} руб.")
    print(f"- Самый популярный ряд: {popular_row}")


def menu():
    print('КИНОТЕАТР "ПРЕМЬЕР"')
    print('Фильм: "Интерстеллар"')
    print("Время: 18:00")
    
    while True:
        show_hall()
        print("\nМеню:")
        print("1. Забронировать место")
        print("2. Отменить бронь")
        print("3. Показать статистику")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            book_seats()
        elif choice == "2":
            cancel_booking()
        elif choice == "3":
            show_stats()
        elif choice == "0":
            print("Спасибо за посещение!")
            break
        else:
            print(" Неверный выбор.")


menu()