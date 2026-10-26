from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
rt(90)
for i in range(3):
    rt(45)
    fd(10*k)
    rt(45)
rt(315)
fd(10*k)
for i in range(2):
    rt(90)
    fd(10*k)
up()
for x in range(-15, 15):
    for y in range(-15, 15):
        teleport(x*k, y*k)
        dot(2, 'red')
print('считаем ручками')
update()
done()