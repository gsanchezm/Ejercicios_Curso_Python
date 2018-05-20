# -*- codif utf-8 -*-

def palindrome_dos(word):
    #Notación slice
    reverse_word = word[:: -1]

    return True if reverse_word == word else False

def palindrome(word):
    reverse_letters = []

    for letter in word:
        reverse_letters.insert(0, letter)

    reverse_word = ''.join(reverse_letters)

    return True if reverse_word == word else False


if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    print('{} sí es palindromo.'.format(word) if palindrome_dos(word) is True else '{} no es palindromo.'.format(word))
