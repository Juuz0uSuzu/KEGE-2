from turtle import *
tracer(0)
screensize(10000, 10000)
left(90)
k=10
for i in range(2):
    fd(13*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(8*k)
rt(90)
bk(3*k)
lt(90)
down()
for i in range(2):
    fd(16*k)
    rt(90)
    fd(8*k)
    rt(90)
for x in range(0, 6):
    for y in range(8, 14):
        teleport(x*k, y*k)
        dot(4, 'red')
print((14*21)+(17*9)-(6*6))
update()
done()