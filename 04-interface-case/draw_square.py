import turtle


def square(t, length):
    for iterator in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()

square(bob, 100)

turtle.mainloop()
