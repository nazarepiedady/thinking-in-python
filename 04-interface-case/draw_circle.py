import turtle

def polygon(t, n, length):
    polygon_angle = 360 / n
    for iterator in range(n):
        t.fd(length)
        t.lt(polygon_angle)

def circle(t, r):
    from draw_arc import arc
    arc(t, r, 360)

bob = turtle.Turtle()

circle(bob, r=50)

turtle.mainloop()
