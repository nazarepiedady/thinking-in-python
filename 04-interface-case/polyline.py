def polyline(t, n, length, angle):
    '''Draw n rect segments with the given width and
    angle (in degrees) between them. t is a turtle.
    '''
    for iterator in range(n):
        t.fd(length)
        t.lt(angle)
