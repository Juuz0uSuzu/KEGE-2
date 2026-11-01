from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(2):
    fd(13*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(5*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(2):
    fd(11*k)
    rt(90)
    fd(7*k)
    rt(90)
for x in range(9, 17):
    for y in range(5, 14):
        teleport(x*k, y*k)
        dot(3 ,'red')
#(R1 - L1) * (R2 - L2)
print((17-9)*(14-5))
update()
done()