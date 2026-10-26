from turtle import *
screensize(10_000, 10_000)
tracer(0)
k=10
left(90)
for i in range(2):
    fd(28*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(14*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(30*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(10, 18):
    for y in range(14, 29):
        teleport(x*k, y*k)
        dot(3, 'red')
print((30+1)*(7+1)+(28+1)*(18+1)-(18-10)*(29-14)) # объединение точек включая линии (s1 + 1) * (s2 + 1) + (s3 + 1) * (s4 + 1) - (R1 - L1) * (R2 - L2)
update()
done()

