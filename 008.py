"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(1)

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'orange', 'red']
for _ in range (29):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(25)