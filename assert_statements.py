from typing import ValuesView


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = input("Ingresa un número: ")
        assert num.isnumeric(), "Debes ingresar un número"
        assert int(num) > 0, "Debes ingresar un número positivo"
        print(divisors(int(num)))
        print("Terminó mi programa")
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    run()