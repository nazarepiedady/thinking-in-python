def area(radius):
    '''
    receive the `radius` value to return the area
    based on given radius value.
    '''
    import math
    a = math.pi * radius ** 2
    return a


_area = area(6.8)

print(_area)
