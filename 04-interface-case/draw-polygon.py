import turtle

def polygon(t, n, length):
    polygon_angle = 360 / n
    for iterator in range(n):
        t.fd(length)
        t.lt(polygon_angle)

bob = turtle.Turtle()

polygon(bob, n=7, length=70)

turtle.mainloop()
