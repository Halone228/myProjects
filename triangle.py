#                                           ТРЕУГОЛНИК СЕРПИНСКОГО.
# Рисовать буду с помощью черепашей графики и l-системы
# Импортирования нужных библиотек
import turtle as te

# Необходимые переменные
axiom = "F-G-G"  # Начальная строка, ну или же аксиома
rule = {"F": "F-G+F+G-F", "G": "GG", "+": "+", "-": "-"}  # Хэш таблица(библиотека) с правилами
temp = ""  # Пустая строка для внесения временных даных
angel = 120  # Угол поворота черепахи

try:
    f = int(input("Введите число итераций:"))
except ValueError:
    print("Вы ввели не число, программа завершилась\n")

for i in range(f):
    for char in axiom:
        temp += rule[char]
    axiom = temp
    temp = ""
# Настройка черепахи
te.hideturtle()
te.up()
screen = te.Screen()
screen.setup(1360, 768)
screen.screensize(1360 * 3, 768 * 3)
te.setposition(-500, -300)
te.pensize(2)# Ширина ребра
te.down()
te.color('blue')
# Рисование
for char in axiom:
    if char == "+":
        te.right(angel)
    elif char == "-":
        te.left(angel)
    else:
        te.forward(10)# Длина ребра
te.done()
