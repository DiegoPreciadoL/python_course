import math

def run():
    # Normal form
    """
    my_dict = {}

    for i in range(1, 101):
        my_dict[i] = i**3

    print(my_dict)
    """
    
    # Dict comprehensions form
    """
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    
    for key, value in my_dict.items():
        print(key, " - ", value)
    """
    # Reto

    my_dict = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}

    for key, value in my_dict.items():
        print(key, " - ", value)


if __name__ == '__main__':
    run()