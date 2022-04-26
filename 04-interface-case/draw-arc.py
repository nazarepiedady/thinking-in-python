import turtle

def arc(t, r, angle):
    from math import pi
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for iterator in range(n):
        t.fd(step_length)
        t.lt(step_angle)


custom_arc = turtle.Turtle()

arc(custom_arc, 60, 90)

turtle.mainloop()
