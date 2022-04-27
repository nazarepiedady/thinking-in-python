import turtle


def circle(t, r):
    from draw_arc import arc
    arc(t, r, 360)

bob = turtle.Turtle()

circle(bob, r=50)

turtle.mainloop()
