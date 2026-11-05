from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10

for i in range(6):
    fd(33*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(6):
    fd(24*k)
    rt(90)
    fd(25*k)
    rt(90)
up()
for x in range(10, 20):
    for y in range(4, 27):
        teleport(x*k, y*k)
        dot(3, 'red')
print(10*23)
update()
done()

