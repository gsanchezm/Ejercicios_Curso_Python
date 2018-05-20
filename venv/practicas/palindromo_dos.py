# -*- coding: utf-8 -*-

def run():
    word = str(input('Escribe una palabra: ')).lower()
    print('{} sí es palindromo.'.format(word) if word == word[::-1] else '{} no es palindromo.'.format(word))

if __name__ == '__main__':
    run()