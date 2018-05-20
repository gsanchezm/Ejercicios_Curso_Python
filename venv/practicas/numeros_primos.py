#-*- coding: utf-8 -*-

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return False
    elif number > 2 and number%2 == 0:
        return False
    else:
        for i in range(3, number):
            return False if number % i == 0 else True

def run():
    number = int(input('Escribe un número: '))
    result = is_prime(number)

    print('Tu número es primo!' if result is True else 'Tu número No es primo!')
    # if result is True:
    #     print('Tu número es primo!')
    # else:
    #     print('Tu número No es primo!')

if __name__ == '__main__':
    run()