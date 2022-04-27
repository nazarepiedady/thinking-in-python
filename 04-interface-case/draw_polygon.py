import turtle

def polygon(t, n, length):
    from polyline import polyline

    polygon_angle = 360 / n
    polyline(t, n, length, polygon_angle)

bob = turtle.Turtle()

polygon(bob, n=7, length=70)

turtle.mainloop()
