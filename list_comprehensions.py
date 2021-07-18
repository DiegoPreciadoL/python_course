def run():
    # squares = []

    # Normal form

    """
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)
    """

    # List comprehensions form
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # print(squares)

    # Reto

    squares = [i for i in range(1, 10000) if i%4 == 0 if i%6 == 0 if i%9 == 0]
    print(squares)


if __name__ == '__main__':
    run()