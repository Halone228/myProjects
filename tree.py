#                                    ДЕРЕВО ПИФАГОРА.
# Рисование с импользование черепашей графики и l-системы

# Импорт необходимых библиотек
import turtle as te
import random

# Необходимые переменные
string = "0"
rule = {"1": "11", "0": "11[0]0", '[': '[', ']': ']'}
temp = ""
# Число итераций чем больше тем больше будет дерево
iterations = int(input("Введите число повторений(будет зависить высота рисунка)"))
stack = []
# Проходка итераций
for i in range(iterations):
    for j in string:
        temp += rule[j]
    string = temp
    temp = ""
# Рисование
# Настройка черепахи
te.hideturtle()
te.up()
screen = te.Screen()
screen.setup(1360, 768)
screen.screensize(1360 * 3, 768 * 3)
te.setposition(0, -300)
te.left(90)
te.pensize(2)
te.down()
te.color('green')
# Основной процесс
for char in string:  # Проходит по строке
    # Условия
    if char == "0":
        te.forward(1)
        print("Вперед 10\n")
    elif char == "1":
        te.forward(1)
        print("Вперед 10\n")
    elif char == "[":
        # Добавления объектов в стек
        stack.append(te.heading())
        stack.append(te.xcor())
        stack.append(te.ycor())
        # Поворот
        te.left(random.randrange(10, 60))
    elif char == "]":
        # Теперь мы в обратном направлении будем удалять объекты из стека, а также переносить их в
        # данные черепахи(примичание: черепаха будет поднята)
        te.up()
        z, d, f = stack.pop(), stack.pop(), stack.pop()
        te.sety(f)
        te.setx(d)
        te.setheading(z)
        te.down()
        print("Поднять кисть\n Возвращения места и угла")
        te.right(random.randrange(10, 60))
te.done()
