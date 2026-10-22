from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(9):
    fd(17*k)
    lt(90)
    fd(8*k)
    lt(90)
    fd(17*k)
up()
lt(90)
fd(3*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(4):
    fd(97*k)
    rt(90)
    fd(132*k)
    rt(90)
up()
for x in range(-5, 1):
    for y in range(-17, -4):
        teleport(x*k, y*k)
        dot(3, 'red')
print(2*(6)+2*(21))
update()
done()
