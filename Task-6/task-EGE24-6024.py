from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(4):
    fd(19*k)
    rt(90)
    fd(30*k)
    rt(90)
up()
fd(2*k)
rt(90)
fd(8*k)
lt(90)
down()
for i in range(4):
    fd(93*k)
    rt(90)
    fd(97*k)
    rt(90)
up()
for x in range(8, 31):
    for y in range(2 ,20):
        teleport(x*k, y*k)
        dot(3, 'red')
print((31-8-1)*(20-2-1))
update()
done()
