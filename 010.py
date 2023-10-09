"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.shape('square')
    turtle.color('blue')
    turtle.forward(100)
    turtle.right(90)

turtle.up()
turtle.backward(20)
turtle.left(90)
turtle.down()

for _ in range(4):
   turtle.shape('triangle')
   turtle.color('black')
   turtle.left(90)
   turtle.forward(100)

turtle.up()
turtle.forward(20)
turtle.left(90)
turtle.backward(20)
turtle.down()

for _ in range(4):
   turtle.shape('circle')
   turtle.color('orange')
   turtle.bk(100)
   turtle.left(90)

turtle.up()
turtle.forward(20)
turtle.left(90)
turtle.down()

for _ in range(4):
   turtle.shape('turtle')
   turtle.color('red')
   turtle.right(90)
   turtle.forward(100)

turtle.up()
turtle.backward(100)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(20)
turtle.left(180)
turtle.down()

turtle.color('pink')
turtle.shape('arrow')

for _ in range(4):
    turtle.forward(260)
    turtle.left(90)

turtle.color('pink')
turtle.shape('arrow')

for _ in range(4):
    turtle.forward(460)
    turtle.left(90)