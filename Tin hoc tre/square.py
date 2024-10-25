from turtle import *

def square(n):
    pendown()
    for i in range(4):
        forward(n)
        left(90)

    left(45)
    forward(n * 2 ** 0.5)
    left(135)
    forward(n)
    left(135)
    forward(n * 2 ** 0.5)
    left(45)

x = 0
y = 0
N = int(input())
d = int(input())
for k in range(N):
    for i in range(N):
        square(d)
    penup()
    y = y + d
    towards(x, y)
mainloop()