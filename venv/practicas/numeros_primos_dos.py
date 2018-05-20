def is_prime(number):
    if number == 1 or number == 2:
        return True
    else:
        for i in range(2, number):
            return False if (number % i == 0) else True

def run():
    print('Recuerde que los numero primos solo se diviven de manera exacta por 1 y por si mismos ')
    number = int(input('Ingrese el numero que desea evaluar si es primo: '))

    print('El numero es primo' if is_prime(number) is True else 'El numero NO es primo')

if __name__ == '__main__':
    run()
