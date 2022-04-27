def polyline(t, n, length, angle):
    for iterator in range(n):
        t.fd(length)
        t.lt(angle)
