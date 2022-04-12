import math

noise_power = 60
signal_power = 20
first_radians = 0.7

ratio = signal_power / noise_power

height = math.sin(first_radians)
decibels = 10 * math.log10(ratio)

print(ratio)
print(height)
print(decibels)

degrees = 45
second_radians = degrees / 180 * math.pi

print(second_radians)
print(math.sin(second_radians))

x = math.sin(degrees / 360.0 * 2 * math.pi)

print(x)

y = math.exp(math.log(x + 1))

print(y)
