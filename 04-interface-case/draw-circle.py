import turtle

def polygon(t, n, length):
    polygon_angle = 360 / n
    for iterator in range(n):
        t.fd(length)
        t.lt(polygon_angle)

def circle(t, r):
    from math import pi
    n = 50
    circumference = 2 * pi * r
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()

circle(bob, r=50)

turtle.mainloop()