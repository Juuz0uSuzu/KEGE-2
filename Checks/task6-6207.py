from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(2):
    fd(35*k)
    rt(90)
    fd(10*k)
    rt(90)
fd(3*k)
lt(90)
fd(15*k)
rt(90)
for i in range(2):
    fd(9*k)
    rt(90)
    fd(32*k)
    rt(90)
for x in range(0, 11):
    for y in range(12, 36):
        teleport(x*k, y*k)
        dot(3,'red')
print((11-0-1)*(36-12-1))
update()
done()
