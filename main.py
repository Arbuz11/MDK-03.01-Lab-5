import math


def get_user_input():
    while True:
        try:
            num = float(input("Введите число: "))
            return num
        except ValueError:
            print("Пожалуйста, введите корректное число.")


def sin_func():
    num = get_user_input()
    result = math.sin(num)
    print(f"Синус числа {num} равен {result}")


def cos_func():
    num = get_user_input()
    result = math.cos(num)
    print(f"Косинус числа {num} равен {result}")


def tan_func():
    num = get_user_input()
    result = math.tan(num)
    print(f"Тангенс числа {num} равен {result}")


def cotan_func():
    num = get_user_input()
    result = 1 / math.tan(num)
    print(f"Котангенс числа {num} равен {result}")


def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Синус")
        print("2. Косинус")
        print("3. Тангенс")
        print("4. Котангенс")
        print("5. Выйти")

        choice = input("Введите номер операции: ")

        if choice == '1':
            sin_func()
        elif choice == '2':
            cos_func()
        elif choice == '3':
            tan_func()
        elif choice == '4':
            cotan_func()
        elif choice == '5':
            print("Заверешние работы программы")
            break
        else:
            print("Пожалуйста, выберите корректную операцию.")


if __name__ == "__main__":
    main()