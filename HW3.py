import sys


balance = 10000
pin_code = None
operations = []
operation_counter = 0
undo_stack = []


def add_operation(op_type, amount, current_balance):
    global operation_counter
    operation_counter += 1
    operations.append({
        "id": operation_counter,
        "type": op_type,
        "amount": amount,
        "balance": current_balance
    })
    undo_stack.append((op_type, amount))


def undo_last_operation():
    global balance

    if not undo_stack:
        print(" Нет операций для отмены.")
        return

    op_type, amount = undo_stack.pop()
    last_op = operations.pop()

    if op_type == "Пополнение":
        balance -= amount
    elif op_type == "Снятие":
        balance += amount
    elif op_type == "Перевод":
        balance += amount  # возвращаем без комиссии для простоты

    print(" Последняя операция отменена.")
    print("Текущий баланс:", balance)


def check_pin():
    global pin_code
    if pin_code is None:
        print("PIN-код ещё не установлен.")
        set_pin()

    attempts = 3
    while attempts > 0:
        entered = input("Введите PIN: ")
        if entered == pin_code:
            print(" Доступ разрешён")
            return True
        attempts -= 1
        print(f"Неверный PIN! Осталось попыток: {attempts}")

    print(" Карта заблокирована")
    sys.exit()


def set_pin():
    global pin_code
    while True:
        new_pin = input("Установите новый PIN: ")
        confirm = input("Подтвердите PIN: ")
        if new_pin == confirm:
            pin_code = new_pin
            print(" PIN установлен")
            break
        else:
            print("PIN не совпадает, попробуйте снова")


def change_pin():
    global pin_code
    old = input("Введите текущий PIN: ")
    if old != pin_code:
        print(" Неверный PIN")
        return
    set_pin()


def show_balance():
    print(f"Ваш баланс: {balance} руб.")


def withdraw():
    global balance
    amount = int(input("Сумма для снятия: "))

    if amount > 5000:
        print(" Максимально можно снять 5000 руб.")
        return

    if amount > balance:
        print(" Недостаточно средств.")
        return

    confirm = input(f"Подтвердить снятие {amount} руб? (да/нет): ")
    if confirm == "да":
        balance -= amount
        add_operation("Снятие", amount, balance)
        print(" Операция выполнена")
        print(f"Возьмите деньги: {amount} руб.")
        show_balance()
    else:
        print("Операция отменена.")


def deposit():
    global balance
    amount = int(input("Сумма для пополнения: "))
    balance += amount
    add_operation("Пополнение", amount, balance)
    print(" Пополнение выполнено")
    show_balance()


def transfer():
    global balance
    amount = int(input("Сумма для перевода: "))

    if amount > balance:
        print(" Недостаточно средств.")
        return

    commission = amount * 0.01
    total = amount + commission

    print(f"Комиссия 1%: {commission:.2f} руб.")
    confirm = input(f"Итого будет списано {total:.2f} руб — подтвердить? (да/нет): ")
    if confirm == "да":
        balance -= total
        add_operation("Перевод", total, balance)
        print(" Перевод выполнен")
        show_balance()
    else:
        print("Операция отменена.")


def show_history():
    if not operations:
        print("Пока нет операций.")
        return
    print("История операций:")
    for op in operations:
        print(f"{op['id']}. {op['type']} {op['amount']} руб. (баланс: {op['balance']} руб.)")


def menu():
    while True:
        print("\n БАНКОМАТ ")
        print("1. Проверить баланс")
        print("2. Снять деньги")
        print("3. Пополнить счёт")
        print("4. Перевести на другой счёт")
        print("5. История операций")
        print("6. Отменить последнюю операцию")
        print("7. Сменить PIN-код")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "4":
            transfer()
        elif choice == "5":
            show_history()
        elif choice == "6":
            undo_last_operation()
        elif choice == "7":
            change_pin()
        elif choice == "0":
            print("Спасибо за использование банкомата!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


print(" БАНКОМАТ ")
check_pin()
menu()
