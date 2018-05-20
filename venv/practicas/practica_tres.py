import turtle


def main():
    window = turtle.Screen()
    gil = turtle.Turtle()
    make_square(gil)
    turtle.mainloop()


def make_square(gil):
    lenght = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line_and_turn(gil, lenght)


def make_line_and_turn(gil, lenght):
    gil.forward(lenght)
    gil.left(90)


if __name__ == '__main__':
    main()
