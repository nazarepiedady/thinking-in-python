import turtle


def square(t, length):
    for iterator in range(4):
        t.fd(100)
        t.lt(length)


bob = turtle.Turtle()

square(bob, 90)

turtle.mainloop()
