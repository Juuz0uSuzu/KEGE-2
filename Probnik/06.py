from turtle import *
screensize(10000, 10000)
tracer(0)
left(90)
k=10
for i in range(8):
    fd(16*k)
    rt(90)
    fd(22*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(8):
    fd(52*k)
    rt(90)
    fd(77*k)
    rt(90)
up()
for x in range(5, 23):
    for y in range(5, 17):
        teleport(x*k, y*k)
        dot(3, 'red')
print((23-5-1)*(17-5-1))
update()
done()