def steps(number):
    # check for valid input; raise exception if not
    if not number > 0: 
        raise ValueError("Only positive integers are allowed")

    count: int = 0
    while True:
        if number == 1:
            return count
        elif number % 2 == 0:
            number //= 2
        else:
            number = (3 * number) + 1
        count += 1
