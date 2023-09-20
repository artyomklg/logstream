def main() -> None:
    print("Введите список чисел через пробел")
    try:
        lst: list[int] = list(map(int, input().strip().split()))
    except ValueError:
        print("Неправильный формат ввода")
        return

    for num in lst:
        if num == 237:
            break
        if num % 2 == 0:
            print(num)


if __name__ == "__main__":
    main()
