def main() -> None:
    try:
        num1: int = float(input("Ввести произвольное число: "))
        num2: int = float(input("Ввести пограничное число: "))
    except ValueError:
        print("Неверный формат ввода")
        return

    if num1 < num2:
        print("1-ое число меньше пограничного")
    else:
        to_print: str = "1-ое число больше пограничного"

        if num1 > num2 * 3:
            to_print = f"{to_print}, причем более чем в 3 раза"
        print(to_print)


if __name__ == "__main__":
    main()
