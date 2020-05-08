def math_func(a):
    return (a - 3) ** 5 - (a - 1) ** 3 + 40

def PoW(guess, PoW_number):
    if guess == math_func(PoW_number):
        return True
    else:
        return False