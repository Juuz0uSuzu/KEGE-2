from pkgutil import resolve_name
from turtle import *
screensize(10_000, 10_000)
tracer(0)
k=10
left(90)
for i in range(2):
    fd(8*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)
for x in range(10, 18):
    for y in range(4, 9):
        teleport(x*k, y*k)
        dot(3, 'red')
#(s1 + 1) * (s2 + 1) + (s3 + 1) * (s4 + 1) - (R1 - L1) * (R2 - L2)
print((8+1)*(18+1)+(17+1)*(7+1)-(9-4)*(18-10))
update()
done()